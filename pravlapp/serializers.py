from rest_framework import serializers
from pravlapp.models import User, Device, Reading, Rule, Message, FirebaseToken


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('id', 'type', 'current_value', 'last_update')
        extra_kwargs = {'id': {'read_only': False, 'required': False}}


class DeviceSerializer(serializers.ModelSerializer):
    readings = ReadingSerializer(many=True)

    class Meta:
        model = Device
        fields = ('id', 'serial_number', 'name', 'heartbeat', 'active', 'readings')

    def create(self, validated_data):
        user = validated_data.pop('user')
        readings = validated_data.pop('readings')
        device = Device.objects.create(user=user, **validated_data)
        for reading in readings:
            Reading.objects.create(device=device, **reading)
        return device

    def update(self, instance, validated_data):
        readings_data = validated_data.pop('readings')
        readings = instance.readings.all()

        instance.heartbeat = validated_data.get('heartbeat', instance.heartbeat)
        instance.active = validated_data.get('active', instance.active)

        instance.save()

        for reading in readings:
            reading_data = filter(lambda r: r['id'] == reading.id, readings_data)[0]
            reading.current_value = reading_data.get('current_value', reading.current_value)
            reading.save()

        return instance


class MessageSerializer(serializers.ModelSerializer):
    class RuleNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Rule
            fields = ('name',)

    rule = RuleNameSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'timestamp', 'rule')


class RuleSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Rule
        fields = ('id', 'name', 'active', 'definition', 'messages')

    def create(self, validated_data):
        return Rule.objects.create(**validated_data)


class FirebaseTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseToken
        fields = ('id', 'token')

    def create(self, validated_data):
        return FirebaseToken.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    rules = RuleSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    tokens = FirebaseTokenSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'devices', 'rules', 'messages', 'tokens')

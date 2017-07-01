from rest_framework import serializers
from pravlapp.models import User, Device, Reading, Rule, Message, FirebaseToken


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('id', 'type', 'current_value', 'last_update')


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


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'timestamp')


class RuleSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Rule
        fields = ('id', 'name', 'active', 'definition', 'messages')


class FirebaseTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseToken
        fields = ('id', 'token')


class UserSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    rules = RuleSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    tokens = FirebaseTokenSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'devices', 'rules', 'messages', 'tokens')

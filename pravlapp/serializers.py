from rest_framework import serializers
from pravlapp.models import User, Device, Reading, Rule, Message, FirebaseToken


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('id', 'type', 'current_value', 'last_update')


class DeviceSerializer(serializers.ModelSerializer):
    readings = ReadingSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = ('id', 'serialNumber', 'name', 'heartbeat', 'active', 'readings')


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

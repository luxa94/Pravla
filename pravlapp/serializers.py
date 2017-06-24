from rest_framework import serializers
from pravlapp.models import User, Device, Reading, Rule, Message, FirebaseToken

# TODO: Finish serializers :)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'serialNumber', 'name', 'heartbeat', 'active')


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('id', 'type','current_value', 'last_update')


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ('id', 'name', 'active', 'definition')


class Message(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'timestamp')


class FirebaseToken(serializers.ModelSerializer):
    class Meta:
        model = FirebaseToken
        fields = ('id', 'token')
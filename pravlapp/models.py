from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(unique=True, max_length=256)
    password = models.CharField(max_length=256)
    email = models.EmailField()


class Device(models.Model):
    serial_number = models.CharField(unique=True, max_length=256)
    name = models.CharField(max_length=256)
    heartbeat = models.IntegerField()
    active = models.BooleanField()
    user = models.ForeignKey(User, related_name="devices")


class Reading(models.Model):
    type = models.CharField(max_length=256)
    current_value = models.FloatField()
    last_update = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Device, related_name="readings")


class Rule(models.Model):
    name = models.CharField(max_length=256)
    active = models.BooleanField()
    definition = models.TextField()
    user = models.ForeignKey(User, related_name="rules")
    devices = models.ManyToManyField(Device)


class Message(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    rule = models.ForeignKey(Rule, related_name="messages")
    user = models.ForeignKey(User, related_name="messages")


class FirebaseToken(models.Model):
    token = models.CharField(max_length=1000)
    user = models.ForeignKey(User, related_name="tokens")


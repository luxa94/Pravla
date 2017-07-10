from pravlapp.models import Device


class SetHeartbeatAction:
    def __init__(self):
        self.device_id = -1
        self.value = 0

    def interpret(self, model):
        self.device_id = model.deviceId
        self.value = model.value

    def validation_errors(self, devices):
        for device in devices:
            if device.id == self.device_id:
                return []
        return [f"Device with id {self.device_id} found in set action doesn't belong to you."]

    def execute(self):
        device = Device.objects.get(pk=self.device_id)
        device.heartbeat = self.value
        device.save()

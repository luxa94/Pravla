class SetHeartbeatAction:
    def __init__(self):
        self.device_id = -1
        self.value = 0

    def interpret(self, model):
        self.device_id = model.deviceId
        self.value = model.value

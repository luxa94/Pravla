class BasicCondition:
    def __init__(self):
        self.device_id = -1
        self.type = ""
        self.comparator = ""
        self.threshold = 0

    def interpret(self, model):
        self.device_id = model.deviceId
        self.type = model.type
        self.comparator = model.comparator
        self.threshold = model.threshold

    def device_ids(self):
        return [self.device_id]

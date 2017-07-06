from pravlapp.models import Reading
from pravlapp.rule.condition import BaseCondition


class BasicCondition(BaseCondition):
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

    def validation_errors(self, devices):
        device = self.find_device(devices, self.device_id)
        if device is None:
            return [f"Device with id {self.device_id} found in rule condition doesn't belong to you."]

        device_readings = list(Reading.objects.filter(device=device))
        reading = self.find_reading(device_readings, self.type)
        print(f'reading type: {self.type}, reading: {reading}')
        if reading is None:
            return [f"Device with id {self.device_id} doesn't have reading of type {self.type}."]

        return []

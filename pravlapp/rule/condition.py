class BaseCondition:
    def find_device(self, devices, device_id):
        for device in devices:
            if device.id == device_id:
                return device
        return None

    def find_reading(self, readings, reading_type):
        for reading in readings:
            if reading.type == reading_type:
                return reading

        return None

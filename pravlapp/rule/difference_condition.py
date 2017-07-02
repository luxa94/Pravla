class DifferenceCondition:

    def  __init__(self):
        self.device_one_id = -1
        self.device_two_id = -1
        self.device_one_type = ""
        self.device_two_type = ""
        self.comparator = ""
        self.difference = 0

    def interpret(self, model):
        self.device_one_id = model.deviceId
        self.device_one_type = model.type1
        self.comparator = model.comparator
        self.device_two_id = model.deviceId2
        self.device_two_type = model.type2
        self.difference = model.difference
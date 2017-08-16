from pravlapp.models import Feed
from pravlapp.rule.condition import BaseCondition

operators = {'<': '+', '>': '-', '<=': '+', '>=': '-'}


class DifferenceCondition(BaseCondition):
    def __init__(self):
        self.device_one_id = -1
        self.device_two_id = -1
        self.device_one_type = ""
        self.device_two_type = ""
        self.comparator = ""
        self.difference = 0

    def interpret(self, model):
        self.device_one_id = model.deviceId1
        self.device_one_type = model.type1
        self.comparator = model.comparator
        self.device_two_id = model.deviceId2
        self.device_two_type = model.type2
        self.difference = 0 if model.difference is None else model.difference

    def device_ids(self):
        return [self.device_one_id, self.device_two_id]

    def validation_errors(self, devices):
        device_one = self.find_device(devices, self.device_one_id)
        if device_one is None:
            return [f"Device with id {self.device_one_id} found in rule condition doesn't belong to you."]

        device_two = self.find_device(devices, self.device_two_id)
        if device_two is None:
            return [f"Device with id {self.device_two_id} found in rule condition doesn't belong to you."]

        device_one_feeds = list(Feed.objects.filter(device=device_one))
        feed_one = self.find_feed(device_one_feeds, self.device_one_type)
        if feed_one is None:
            return [f"Device with id {self.device_one_id} doesn't have feed of type {self.device_one_type}."]

        device_two_feeds = list(Feed.objects.filter(device=device_two))
        feed_two = self.find_feed(device_two_feeds, self.device_two_type)
        if feed_two is None:
            return [f"Device with id {self.device_two_id} doesn't have feed of type {self.device_two_type}."]

        if self.device_one_type != self.device_two_type:
            return [f'Found different types in same condition ({self.device_one_type} and {self.device_two_type}).']

        if self.device_one_id == self.device_two_id:
            return [f"Device with id {self.device_one_id} can't be compared to itself."]

        return []

    def applies_for(self, devices):
        device_one = self.find_device(devices, self.device_one_id)
        device_two = self.find_device(devices, self.device_two_id)

        feed_one = self.find_feed(device_one.feeds, self.device_one_type)
        feed_two = self.find_feed(device_two.feeds, self.device_two_type)

        return eval(f'{feed_one.current_value} {operators[self.comparator]} {self.difference} {self.comparator} {feed_two.current_value}')

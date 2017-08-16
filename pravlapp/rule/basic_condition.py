from pravlapp.models import Feed
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

        device_feeds = list(Feed.objects.filter(device=device))
        feed = self.find_feed(device_feeds, self.type)
        print(f'feed type: {self.type}, feed: {feed}')
        if feed is None:
            return [f"Device with id {self.device_id} doesn't have feed of type {self.type}."]

        return []

    def applies_for(self, devices):
        device = self.find_device(devices, self.device_id)
        feed = self.find_feed(Feed.objects.filter(device=device), self.type)
        return eval(f'{feed.current_value} {self.comparator} {self.threshold}')


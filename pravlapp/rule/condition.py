class BaseCondition:
    def find_device(self, devices, device_id):
        for device in devices:
            if device.id == device_id:
                return device
        return None

    def find_feed(self, feeds, feed_type):
        for feed in feeds:
            if feed.type == feed_type:
                return feed

        return None

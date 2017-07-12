import itertools
import datetime

from pravlapp.models import Device
from pravlapp.rule.basic_condition import BasicCondition
from pravlapp.rule.composite_condition import CompositeCondition
from pravlapp.rule.difference_condition import DifferenceCondition
from pravlapp.rule.send_action import SendAction
from pravlapp.rule.set_heartbeat_action import SetHeartbeatAction

all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class ParsedRule:
    def __init__(self):
        self.days = []
        self.condition = None
        self.send_actions = []
        self.set_actions = []

    def interpret(self, model):
        condition_class_name = model.condition.__class__.__name__
        if condition_class_name == 'BasicCondition':
            self.condition = BasicCondition()
            self.condition.interpret(model.condition)
        elif condition_class_name == 'DifferenceCondition':
            self.condition = DifferenceCondition()
            self.condition.interpret(model.condition)
        else:  # CompositeCondition
            self.condition = CompositeCondition()
            self.condition.interpret(model.condition)

        for action in model.actions:
            action_class_name = action.__class__.__name__
            if action_class_name == 'SendAction':
                new_action = SendAction()
                new_action.interpret(action)
                self.send_actions.append(new_action)
            else:  # SetHeartbeatAction
                new_action = SetHeartbeatAction()
                new_action.interpret(action)
                self.set_actions.append(new_action)

        self.days = model.days

        if model.days is None or len(model.days) == 0:
            self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def device_ids(self):
        return list(set(self.condition.device_ids()))

    def set_action_device_ids(self):
        return [action.device_id for action in self.set_actions]

    def validation_errors(self, user):
        user_devices = list(Device.objects.filter(user=user))

        errors_condition = self.condition.validation_errors(user_devices)
        errors_action = list(itertools.chain(*[action.validation_errors(user_devices) for action in self.set_actions]))

        return errors_condition + errors_action

    def applies_for(self, devices):
        today = all_days[datetime.datetime.now().weekday()]
        if today in self.days:
            return self.condition.applies_for(devices)
        return False

    def execute_actions(self, user):
        for set_action in self.set_actions:
            set_action.execute()
        for send_action in self.send_actions:
            send_action.execute(user)

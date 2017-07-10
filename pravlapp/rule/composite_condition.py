from pravlapp.rule.basic_condition import BasicCondition
from pravlapp.rule.difference_condition import DifferenceCondition
import itertools

neutral_values = {'or': False, 'and': True}


class CompositeCondition:
    def __init__(self):
        self.operator = ""
        self.conditions = []

    def interpret(self, model):
        self.operator = model.operator

        for model_condition in model.conditions:
            if model_condition.__class__.__name__ == "BasicCondition":
                basic_condition = BasicCondition()
                basic_condition.interpret(model_condition)
                self.conditions.append(basic_condition)

            elif model_condition.__class__.__name__ == "DifferenceCondition":
                difference_condition = DifferenceCondition()
                difference_condition.interpret(model_condition)
                self.conditions.append(difference_condition)

            elif model_condition.__class__.__name__ == "CompositeCondition":
                composite_condition = CompositeCondition()
                composite_condition.interpret(model_condition)
                self.conditions.append(composite_condition)

    def device_ids(self):
        return list(itertools.chain(*[condition.device_ids() for condition in self.conditions]))

    def validation_errors(self, devices):
        return list(itertools.chain(*[condition.validation_errors(devices) for condition in self.conditions]))

    def applies_for(self, devices):
        neutral_value = neutral_values[self.operator]

        for condition in self.conditions:
            applies = condition.applies_for(devices)
            if applies != neutral_value:
                return applies

        return neutral_value

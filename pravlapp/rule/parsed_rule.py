class ParsedRule:
    def __init__(self):
        self.days = []
        self.condition = None
        self.send_actions = []
        self.set_actions = []

    def interpret(self, model):
        condition_class_name = model.condition.__class__.__name__
        if condition_class_name == 'BasicCondition':
            pass
        elif condition_class_name == 'DifferenceCondition':
            pass
        else:  # CompositeCondition
            pass

        for action in model.actions:
            action_class_name = action.__class__.__name__
            if action_class_name == 'SendAction':
                pass
            else:  # SetHeartBeatAction
                pass

        if model.days is None or len(model.days) == 0:
            self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
class SendAction:
    def __init__(self):
        self.command = ''
        self.text = ''

    def interpret(self, model):
        self.command = model.command
        self.text = model.text

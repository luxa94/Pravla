from pravlapp.util.email_util import send_email
from pravlapp.util.notification_util import send_notification


class SendAction:
    def __init__(self):
        self.command = ''
        self.text = ''

    def interpret(self, model):
        self.command = model.command
        self.text = model.text

    def execute(self, user):
        if self.command == 'email':
            send_email(user.email, self.text)
        else:
            for token in user.tokens:
                send_notification(self.text, token)

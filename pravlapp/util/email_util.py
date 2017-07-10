from django.core.mail import send_mail

from Pravla import settings


def send_email(to_email, message):
    subject = 'Pravlo se javlo!'

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST,
        [to_email],
        fail_silently=True
    )

from django.core.mail import send_mail

send_mail(
    'Subject',
    'Pravloooo',
    '',
    ['jasnaa994@gmail.com'],
    fail_silently = False
)
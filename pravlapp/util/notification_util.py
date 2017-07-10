import requests
from Pravla import settings


def send_notification(message, token):
    data = {
        'to': token,
        'notification': {
            'title': 'Pravlo se javlo!',
            'body': message
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'key={settings.FIREBASE_API_KEY}'
    }

    requests.post('https://fcm.googleapis.com/fcm/send', data=data, headers=headers)

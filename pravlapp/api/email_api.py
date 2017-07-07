from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Pravla import settings


class EmailSender(APIView):

    def post(self, request):
        recipient = request.data.get('recipient')
        message = request.data.get('message')
        subject = request.data.get('subject')

        success = send_mail(
            subject,
            message,
            settings.EMAIL_HOST,
            [recipient],
            fail_silently=False
        )

        if success == 1:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
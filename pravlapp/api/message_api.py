from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pravlapp.models import Message
from pravlapp.serializers import MessageSerializer
from pravlapp.util.decorators import Authenticated


class MessageList(APIView):
    @Authenticated
    def get(self, request, user):
        messages = Message.objects.filter(user=user)
        serializer = MessageSerializer(messages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

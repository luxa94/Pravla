from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pravlapp.serializers import RuleSerializer
from pravlapp.util.decorators import Authenticated


class RuleList(APIView):
    @Authenticated
    def post(self, request, user):
        serializer = RuleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

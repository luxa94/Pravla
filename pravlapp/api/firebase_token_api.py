from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from pravlapp.serializers import FirebaseTokenSerializer
from pravlapp.util.decorators import Authenticated


class FirebaseTokenDetail(APIView):
    @Authenticated
    def post(self, request, user):
        serializer = FirebaseTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

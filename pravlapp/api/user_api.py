from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from pravlapp.serializers import UserSerializer


class UserDetail(APIView):
    def post(self, request):
        print(request.data)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

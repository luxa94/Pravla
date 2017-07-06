from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pravlapp.models import Device
from pravlapp.serializers import DeviceSerializer
from pravlapp.util.decorators import Authenticated


class DeviceDetail(APIView):
    def get_object(self, pk):
        try:
            return Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404

    @Authenticated
    def get(self, request, user, pk):
        device = self.get_object(pk)
        if device.user_id != user.id:
            raise Http404

        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    @Authenticated
    def put(self, request, user, pk):
        device = self.get_object(pk)
        if device.user_id != user.id:
            raise Http404

        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceList(APIView):
    @Authenticated
    def post(self, request, user):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @Authenticated
    def get(self, request, user):
        devices = Device.objects.filter(user=user)
        serializer = DeviceSerializer(devices, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

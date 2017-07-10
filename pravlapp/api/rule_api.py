from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pravlapp.models import Device, Rule
from pravlapp.serializers import RuleSerializer
from pravlapp.util.decorators import Authenticated
from pravlapp.util.rule_parser import parse_rule


class RuleDetails(APIView):
    def get_object(self, pk):
        try:
            return Rule.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404

    @Authenticated
    def get(self, request, user, pk):
        rule = self.get_object(pk)
        if rule.user_id != user.id:
            raise Http404

        serializer = RuleSerializer(rule)
        return Response(serializer.data)

    @Authenticated
    def put(self, request, user, pk):
        rule = self.get_object(pk)
        if rule.user_id != user.id:
            raise Http404

        serializer = RuleSerializer(rule, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        rule_definition = request.data['definition']
        parsed_rule = parse_rule(rule_definition)
        if parsed_rule is None:
            return Response({'errors': ["Rule definition invalid."]}, status=status.HTTP_400_BAD_REQUEST)

        validation_errors = parsed_rule.validation_errors(user)
        if len(validation_errors):
            return Response({'errors': validation_errors}, status=status.HTTP_400_BAD_REQUEST)

        devices = list(Device.objects.filter(id__in=parsed_rule.device_ids()))
        serializer.save(user=user, devices=devices)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RuleList(APIView):
    @Authenticated
    def get(self, request, user):
        rules = Rule.objects.filter(user=user)
        serializer = RuleSerializer(rules, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @Authenticated
    def post(self, request, user):
        serializer = RuleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        rule_definition = request.data['definition']
        parsed_rule = parse_rule(rule_definition)
        if parsed_rule is None:
            return Response({'errors': ["Rule definition invalid."]}, status=status.HTTP_400_BAD_REQUEST)

        validation_errors = parsed_rule.validation_errors(user)
        if len(validation_errors):
            return Response({'errors': validation_errors}, status=status.HTTP_400_BAD_REQUEST)

        devices = list(Device.objects.filter(id__in=parsed_rule.device_ids()))
        serializer.save(user=user)
        serializer.save(user=user, devices=devices)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @Authenticated
    def get(self, request, user):
        devices = Rule.objects.filter(user=user)
        serializer = RuleSerializer(devices, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from textx.metamodel import metamodel_from_file

from pravlapp.models import Device
from pravlapp.rule.parsed_rule import ParsedRule
from pravlapp.serializers import RuleSerializer
from pravlapp.util.decorators import Authenticated


class RuleList(APIView):
    @Authenticated
    def post(self, request, user):
        serializer = RuleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        rule_mm = metamodel_from_file('metamodel/rule.tx')
        rule_model = rule_mm.model_from_str(request.data['definition'])
        rule = ParsedRule()
        rule.interpret(rule_model)
        devices = list(Device.objects.filter(id__in=rule.device_ids()))

        serializer.save(user=user)
        serializer.save(user=user, devices=devices)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

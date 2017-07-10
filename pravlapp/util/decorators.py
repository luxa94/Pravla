from rest_framework import status
from rest_framework.response import Response

from pravlapp.models import User


def unauthorized(*args, **kwargs):
    return Response(status=status.HTTP_401_UNAUTHORIZED)


def Authenticated(func):
    def wrapped(self, request, *args, **kwargs):
        principal_id = -1
        try:
            principal_id = request.META['HTTP_AUTHORIZATION']
        except KeyError:
            return unauthorized()
        except User.DoesNotExist:
            return unauthorized()

        if principal_id == -1:
            return unauthorized()

        user = User.objects.get(id=principal_id)
        return func(self, request=request, user=user, *args, **kwargs)

    return wrapped

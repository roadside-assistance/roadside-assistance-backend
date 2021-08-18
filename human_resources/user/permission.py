from pprint import pprint

from rest_framework import permissions
from rest_framework.request import Request

from human_resources.user.model import UserModel
from human_resources.utill.password import pass_gen


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        if 'HTTP_PHONE' not in request.META.keys():
            return False

        phone_number = request.META['HTTP_PHONE']
        password = request.META['HTTP_PASSWORD']
        encoded_password = pass_gen(password)
        return UserModel.objects.filter(phone_number=phone_number, password=encoded_password).count() == 1

    def has_object_permission(self, request, view, obj):
        return True

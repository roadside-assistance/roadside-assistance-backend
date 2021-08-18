from pprint import pprint

from rest_framework import permissions
from rest_framework.request import Request

from human_resources.citizen.model import CitizenModel
from human_resources.inspector.model import InspectorModel
from human_resources.user.model import UserModel
from human_resources.utill.password import pass_gen


class IsInspector(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        phone_number = request.META['HTTP_PHONE']
        password = request.META['HTTP_PASSWORD']
        return self.is_inspector(password, phone_number)

    @staticmethod
    def is_inspector(phone_number, password):
        encoded_password = pass_gen(password)
        return InspectorModel.objects.filter(phone_number=phone_number, password=encoded_password).count() == 1

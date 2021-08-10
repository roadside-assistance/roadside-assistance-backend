from rest_framework import viewsets

from human_resources.citizen.model import Citizen
from human_resources.citizen.serializer import CitizenSerializer
from human_resources.user.permission import IsAuthenticated


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
    permission_classes = [IsAuthenticated]

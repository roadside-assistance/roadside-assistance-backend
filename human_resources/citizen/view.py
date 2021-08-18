from rest_framework import viewsets

from human_resources.citizen.model import CitizenModel
from human_resources.citizen.serializer import CitizenSerializer


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = CitizenModel.objects.all()
    serializer_class = CitizenSerializer

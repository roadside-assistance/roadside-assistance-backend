from rest_framework import viewsets

from human_resources.user.permission import IsAuthenticated
from machine_resources.machine.model import MachineModel
from machine_resources.machine.serializer import MachineSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = MachineModel.objects.all()
    serializer_class = MachineSerializer
    # permission_classes = [IsAuthenticated]

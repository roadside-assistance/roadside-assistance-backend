from rest_framework import viewsets
from human_resources.worker.model import WorkerModel
from human_resources.worker.serializer import WorkerSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = WorkerModel.objects.all()
    serializer_class = WorkerSerializer

    # permission_classes = [IsAuthenticated, IsInspector ]

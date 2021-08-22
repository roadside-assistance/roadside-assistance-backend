from rest_framework import viewsets

from human_resources.inspector.model import InspectorModel
from human_resources.inspector.permission import IsInspector
from human_resources.inspector.serializer import InspectorSerializer
from human_resources.user.permission import IsAuthenticated


class InspectorViewSet(viewsets.ModelViewSet):
    queryset = InspectorModel.objects.all()
    serializer_class = InspectorSerializer

    # permission_classes = [IsAuthenticated,
                          #IsInspector
# ]

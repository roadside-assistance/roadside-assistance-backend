from rest_framework import serializers

from human_resources.inspector.model import InspectorModel
from human_resources.team.model import TeamModel
from human_resources.utill.password import pass_gen
from human_resources.worker.model import WorkerModel


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerModel
        fields = '__all__'


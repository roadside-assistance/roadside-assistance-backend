from rest_framework import serializers

from human_resources.inspector.model import InspectorModel
from human_resources.team.model import TeamModel
from human_resources.utill.password import pass_gen


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'


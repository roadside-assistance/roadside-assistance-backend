from rest_framework import viewsets

from human_resources.user.permission import IsAuthenticated
from problem_solving.skill.model import SkillModel
from problem_solving.skill.serializer import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = [IsAuthenticated]

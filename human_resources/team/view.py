from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from human_resources.team.model import TeamModel
from human_resources.team.serializer import TeamSerializer
from problem_solving.problem.model import ProblemModel
from problem_solving.problem.serializer import ProblemSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = TeamModel.objects.all()
    serializer_class = TeamSerializer

    # permission_classes = [IsAuthenticated, IsInspector ]

    @action(detail=True)
    def assigned_problems(self, request, pk=None):
        team_id = pk
        problems = ProblemModel.objects.filter(assigned_to_team_id=team_id)

        # page = self.paginate_queryset(problems)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data)

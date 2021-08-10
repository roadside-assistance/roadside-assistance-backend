from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from human_resources.citizen.permission import IsCitizen
from human_resources.user.permission import IsAuthenticated
from problem_solving.problem.model import ProblemModel
from problem_solving.problem.serializer import ProblemSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = ProblemModel.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated, IsCitizen]


class IssueProblemView(APIView):
    def post(self, request: Request):
        problem = ProblemModel()
        problem.description = request.data['description']
        problem.address = request.data['address']
        problem.type = request.data['type']
        problem.issuer_id = 1
        problem.save()

        return Response(status=status.HTTP_201_CREATED)


class GetAssignedProblems(APIView):
    def get(self, request: Request):
        problem = ProblemModel.objects.get(id=2)

        return Response({
            'id': problem.id,
            'type': problem.type,
            'description': problem.description,
            'address': problem.address,
        })


class ConfirmProblem(APIView):
    def post(self, request: Request):
        problem = ProblemModel.objects.get(id=request.data['id'])
        problem.status = 'approved'
        problem.needed_devices = request.data['needed_devices']
        problem.save()
        return Response(status=status.HTTP_200_OK)


class GetAssignedMission(APIView):
    def get(self, request: Request):
        problem = ProblemModel.objects.get(id=2)
        return Response({
            'id': problem.id,
            'type': problem.type,
            'description': problem.description,
            'address': problem.address,
            'needed_devices': problem.needed_devices,
        })

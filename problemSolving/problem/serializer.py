from rest_framework import serializers

from problemSolving.problem.model import ProblemModel


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemModel

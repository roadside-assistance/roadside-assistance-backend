from rest_framework import serializers


from problem_solving.problem.model import ProblemModel


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemModel
        fields = '__all__'

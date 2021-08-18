from rest_framework import serializers

from problem_solving.skill.model import SkillModel


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = '__all__'

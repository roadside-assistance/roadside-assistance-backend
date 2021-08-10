from rest_framework import serializers

from human_resources.citizen.model import Citizen
from human_resources.utill.password import pass_gen


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        encoded_password = pass_gen(password)
        validated_data['password'] = encoded_password
        user = Citizen.objects.create(**validated_data)
        return user

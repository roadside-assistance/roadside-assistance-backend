from rest_framework import serializers

from human_resources.inspector.model import InspectorModel
from human_resources.utill.password import pass_gen


class InspectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectorModel
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        encoded_password = pass_gen(password)
        validated_data['password'] = encoded_password
        user = InspectorModel.objects.create(**validated_data)
        return user

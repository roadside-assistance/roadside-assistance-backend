from rest_framework import serializers

from machine_resources.machine.model import MachineModel


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineModel
        fields = '__all__'

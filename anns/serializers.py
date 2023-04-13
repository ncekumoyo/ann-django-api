from rest_framework import serializers
from .models import Ann


class AnnSerializer(serializers.ModelSerializer):
    entity_name = serializers.CharField(
        source='entity.name')
    department_name = serializers.CharField(
        source='department.name')
    entity_logo = serializers.CharField(
        source='entity.logo')
    department_logo = serializers.CharField(
        source='department.logo')

    class Meta:
        model = Ann
        fields = ['id', 'date_created', 'entity_name', 'entity_logo', 'department_name', 'department_logo',
                  'title', 'venue', 'start', 'end', 'info', 'poster']

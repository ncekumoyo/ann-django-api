from rest_framework import serializers
from .models import Ann


class AnnSerializer(serializers.ModelSerializer):
    entity_name = serializers.StringRelatedField(
        source='entity')
    department_name = serializers.StringRelatedField(
        source='department')

    class Meta:
        model = Ann
        fields = ['id', 'date_created', 'entity_name', 'department_name',
                  'title', 'venue', 'start', 'end', 'info', 'poster']

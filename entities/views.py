from rest_framework import generics
from .models import Entity
from .serializers import EntitySerializer


class EntityListCreateView(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

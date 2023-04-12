from rest_framework import generics
from .models import Ann
from .serializers import AnnSerializer


class AnnListCreateView(generics.ListCreateAPIView):
    queryset = Ann.objects.all()
    serializer_class = AnnSerializer

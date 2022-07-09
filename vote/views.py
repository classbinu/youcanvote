from rest_framework import viewsets
from .models import Vote
from .serializers import VoteSerializer
from django_filters.rest_framework import DjangoFilterBackend


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all().order_by('-created')
    serializer_class = VoteSerializer
    permission_classes = []
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['subject']
    # ordering_fields = '__all__'
    # ordering = ['-created']

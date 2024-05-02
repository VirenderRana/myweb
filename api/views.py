# doc_analysis/views.py
from rest_framework import viewsets
from .models import Project, ConfigModel
from .serializers import ProjectSerializer, ConfigModelSerializer

import logging

logger = logging.getLogger(__name__)
class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ConfigModelViewSet(viewsets.ModelViewSet):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer

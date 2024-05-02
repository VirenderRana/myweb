from rest_framework import serializers
from .models import Project,  ConfigModel
import logging

logger = logging.getLogger(__name__)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ConfigModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigModel
        fields = '__all__'


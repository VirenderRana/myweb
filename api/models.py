from django.db import models
#from django.contrib.postgres.fields import JSONField 
from django.db.models import JSONField
import uuid

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    client = models.CharField(max_length=255, null=True)
    project_type = models.CharField(max_length=100, null=True)
    edition = models.CharField(max_length=100, null=True)
    version = models.CharField(max_length=10, null=True)
    sequence_number = models.CharField(max_length=10, null=True)
    description = models.TextField(blank=True, null=True)
    span = models.CharField(max_length=100, blank=True, null=True)
    pick = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.client}"


class ConfigModel(models.Model):
    model_name = models.CharField(max_length=255)
    mcc = models.CharField(max_length=100, default=uuid.uuid4, editable=False)
    fields_data = JSONField()
    last_update = models.DateTimeField(auto_now=True)
    associated_configs = models.JSONField(default=list)

    def __str__(self):
        return self.model_name 


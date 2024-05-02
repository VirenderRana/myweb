# doc_analysis/urls.py

from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from .views import ProjectView
from .views import ConfigModelViewSet



project_router = routers.SimpleRouter()
project_router.register(r'projects', ProjectView)

config_router = DefaultRouter()
config_router.register(r'configmodels', ConfigModelViewSet)

urlpatterns = [
    path('', include(project_router.urls)),
    path('', include(config_router.urls)),
]

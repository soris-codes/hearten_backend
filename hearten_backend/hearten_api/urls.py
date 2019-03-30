from django.urls import path, include 
from .api import PostViewSet  
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/posts', PostViewSet, base_name='posts')
urlpatterns = router.urls
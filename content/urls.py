from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet, basename = "post")
router.register('cv', views.CvViewSet, basename = "cv")

urlpatterns = [
    path('', include(router.urls))
]
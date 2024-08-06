from django.urls import path,include
from .views import Notes
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'notes', Notes, basename='Note')

urlpatterns = router.urls
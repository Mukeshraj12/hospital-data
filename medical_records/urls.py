from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from medical_records.views import UserProfileViewSet, VisitorDataViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'visitordata', VisitorDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]



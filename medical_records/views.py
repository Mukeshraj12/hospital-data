from rest_framework import viewsets
from .models import UserProfile, VisitorData
from .serializers import UserProfileSerializer, VisitorDataSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class VisitorDataViewSet(viewsets.ModelViewSet):
    queryset = VisitorData.objects.all()
    serializer_class = VisitorDataSerializer


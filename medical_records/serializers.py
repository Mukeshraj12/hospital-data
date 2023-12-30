from rest_framework import serializers
from .models import UserProfile, VisitorData, VisitDetail
from django.contrib.auth.models import User

class VisitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitDetail
        fields = ['diagnosis', 'diag_date', 'prescription']

class VisitorDataSerializer(serializers.ModelSerializer):
    visit_details = VisitDetailSerializer(many=True, read_only=True)

    class Meta:
        model = VisitorData
        fields = ['doctor_name', 'admit_date', 'current_progress', 'visit_details']

class UserProfileSerializer(serializers.ModelSerializer):
    visitor_data = VisitorDataSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['admit_id', 'hospital', 'visitor_data']

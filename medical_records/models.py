from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admit_id = models.IntegerField(unique=True)
    hospital = models.CharField(max_length=50)

class VisitorData(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='visitor_data')
    doctor_name = models.CharField(max_length=50)
    admit_date = models.DateField()
    current_progress = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

class VisitDetail(models.Model):
    visitor_data = models.ForeignKey(VisitorData, on_delete=models.CASCADE, related_name='visit_details')
    diagnosis = models.CharField(max_length=100)
    diag_date = models.DateField()
    prescription = models.CharField(max_length=100)

from django.db import models

# Create your models here.
from account.models import UserAccount
from patient.models import Patient


class Intervention(models.Model):
    name = models.CharField(max_length=300, unique=True, primary_key=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    

class Treatment(models.Model):
  user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
  patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
  treatmentstatus = models.CharField(max_length=100)
  statuspayment = models.CharField(max_length=100)
  interventions = models.TextField()
  treatmentamount = models.PositiveIntegerField()
  partpatient = models.IntegerField()
  partinsurance = models.IntegerField()
  partinsurance2 = models.IntegerField(null=True, blank=True)
  partinsurance3 = models.IntegerField(null=True, blank=True)
  updated_on = models.DateTimeField(auto_now=True)
  registered_on = models.DateField(auto_now_add=True)
  class Meta:
        ordering = ['-registered_on']

  def __str__(self):
        return f'{self.id} - {"du patient"} {self.patient}'


from django.db import models
from insurance.models import Insurance,Insurance2,Insurance3
# Create your models here.
from account.models import UserAccount


class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE = "MALE", 'Male'
        FEMELE = "FEMELE", 'Femele'
        OTHER = "OTHER", 'Autre'

    gender = models.CharField(max_length=15, choices=Gender.choices)

    insurance = models.ForeignKey(Insurance, on_delete=models.DO_NOTHING)
    insurance2 = models.ForeignKey(Insurance2, on_delete=models.DO_NOTHING, null=True, blank=True)
    insurance3 = models.ForeignKey(Insurance3, on_delete=models.DO_NOTHING, null=True, blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    profession = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    insurance_matricule = models.CharField(blank=True, null=True, max_length=200)
    insurance_pourcentage = models.IntegerField(blank=True, null=True)
    insurance2_matricule = models.CharField(blank=True, null=True, max_length=200)
    insurance2_pourcentage = models.IntegerField(blank=True, null=True)
    insurance3_matricule = models.CharField(blank=True, null=True, max_length=200)
    insurance3_pourcentage = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} - {self.lastname}'


class PatientMessage(models.Model):
  user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
  subject = models.CharField(max_length=200)
  message = models.TextField()

  updated_on = models.DateTimeField(auto_now=True)
  registered_on = models.DateTimeField(auto_now_add=True)
  class Meta:
        ordering = ['-registered_on']

  def __str__(self):
        return f'{"Message N°"}-{self.id} - {self.subject}'


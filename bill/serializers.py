from .models import Payment
from account.serializers import FirstnameLastnameSerializer
from patient.serializers import PatientLimitedInfoSerializer

from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class UpdatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amountpaid']


class PaymentInfoSerializer(serializers.ModelSerializer):
    # patient = PatientLimitedInfoSerializer()
    user = FirstnameLastnameSerializer()
    class Meta:
        model = Payment
        fields = '__all__'

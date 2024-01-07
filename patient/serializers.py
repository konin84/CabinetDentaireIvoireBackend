from rest_framework import serializers

from .models import Patient, PatientMessage
from insurance.serializers import InsurancenameSerializer
from account.serializers import AccountInfoForMessageSerializer

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class PatientWithInsuranceSerializer(serializers.ModelSerializer):
    insurance =InsurancenameSerializer()
    class Meta:
        model = Patient
        fields = '__all__'


class PatientLimitedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'firstname', 'lastname', 'insurance', 'insurance2','telephone']

# The following codes are for the users to send messages to send messages
class PatientMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMessage
        fields = '__all__'


class PatientMessageInfoSerializer(serializers.ModelSerializer):
    user = AccountInfoForMessageSerializer()
    class Meta:
        model = PatientMessage
        fields = '__all__'


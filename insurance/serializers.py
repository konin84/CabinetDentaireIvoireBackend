from rest_framework import serializers

from .models import Insurance,Insurance2


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class InsurancenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['insurancename', 'id']


class Insurance2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance2
        fields = '__all__'


class Insurance2nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance2
        fields = ['insurancename', 'id']


# class Insurance3Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Insurance3
#         fields = '__all__'


# class Insurance3nameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Insurance3
#         fields = ['insurancename', 'id']

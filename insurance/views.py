from django.shortcuts import render
from .serializers import InsuranceSerializer, Insurance2Serializer
# , Insurance3Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, APIView
#  importing models
from .models import Insurance, Insurance2
# , Insurance3
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def insuranceData(request):

    if request.method == 'GET':
        data = Insurance.objects.all()
        serializer = InsuranceSerializer(data, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialiazer = InsuranceSerializer(data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'Adding new insurance': serialiazer.data}, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def PublicInsuranceData(request):

    if request.method == 'GET':
        data = Insurance.objects.all()
        serializer = InsuranceSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def InsuranceSetting(request, pk):
    try:
        data = Insurance.objects.get(insurancename=pk)
    except Insurance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiazer = InsuranceSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialiazer = InsuranceSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'Insurance': serialiazer.data}, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2ND INSURANCE
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def insurance2Data(request):
    if request.method == 'GET':
        data = Insurance2.objects.all()
        serializer = Insurance2Serializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialiazer = Insurance2Serializer(data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'Adding new insurance': serialiazer.data}, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Insurance2Setting(request, pk):
    try:
        data = Insurance2.objects.get(insurancename=pk)
    except Insurance2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiazer = Insurance2Serializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialiazer = Insurance2Serializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response( serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


# 3RD INSURANCE
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def insurance3Data(request):

#     if request.method == 'GET':
#         data = Insurance3.objects.all()
#         serializer = Insurance3Serializer(data, many=True)

#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         serialiazer = Insurance3Serializer(data=request.data)
#         if serialiazer.is_valid():
#             serialiazer.save()
#             return Response({'Adding new insurance': serialiazer.data}, status=status.HTTP_200_OK)
#         return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated, IsAdminUser])
# def Insurance3Setting(request, pk):
#     try:
#         data = Insurance3.objects.get(insurancename=pk)
#     except Insurance3.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serialiazer = Insurance3Serializer(data)
#         return Response(serialiazer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         data.delete()
#         return Response(status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serialiazer = Insurance3Serializer(data, data=request.data)
#         if serialiazer.is_valid():
#             serialiazer.save()
#             return Response( serialiazer.data, status=status.HTTP_200_OK)
#         return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

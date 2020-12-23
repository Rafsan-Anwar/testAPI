from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import ContactSerializer
from .models import Contact

@api_view(['GET','POST'])
def allContacts(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def oneContact(request, id):
    try:
        contact = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ContactSerializer(contact, many=False)
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ContactSerializer(instance=contact,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        contact.delete()
        return Response('Item succesfully deleted!')


@api_view(['GET','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def hitLike(request, name):
    user = User.objects.get(username__iexact = name)
    pass
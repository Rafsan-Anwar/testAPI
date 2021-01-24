from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# from rest_framework.viewsets import
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *

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


# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
@api_view(['GET','PUT','DELETE'])
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
        try:
            contact = Contact.objects.get(id=id)
            contact.delete()
            return Response(status.HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def hitLike(request, name):
    user = User.objects.get(username__iexact = name)
    pass

@api_view(['GET','POST'])
def allStudent(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        print(request.data)
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def oneStudent(request):
    if request.query_params["id"]:
        try:
            student = Student.objects.get(id=request.query_params["id"])
        except Student.DoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)

        if request.method == 'GET':
            serializer = StudentSerializer(student, many=False)
            return Response(serializer.data, status.HTTP_200_OK)

        if request.method == 'PUT':
            serializer = StudentSerializer(instance=student,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            student.delete()
            return Response('Item succesfully deleted!')
    else:
        return Response("Didn't worked")


@api_view(['GET', 'POST', 'PUT','DELETE'])
def detailsStudent(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        try:
            detailedStudent = DetailedStudent.objects.get(student=student)
            serializer = DetailedStudentSerializer(detailedStudent, many=False)
            print(serializer.data)
            return Response(serializer.data, status.HTTP_200_OK)
        except DetailedStudent.DoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            data = request.data
            detail = DetailedStudent.objects.create(
                student=Student.objects.get(id=data["id"]), bloodGroup = data["bloodGroup"], address = data["address"])
            detail.save()
            serializer = DetailedStudentSerializer(detail, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        detailstudent = DetailedStudent.objects.get(student=student)
        serializer = DetailedStudentSerializer(instance=detailstudent,data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == 'DELETE':
        return Response('Not allowed by system')

@api_view(['GET', 'POST', 'PUT','DELETE'])
def studentsClass(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        try:
            detailedStudent = StudentClass.objects.get(student=student)
            serializer = StudentClassSerializer(detailedStudent, many=False)

            return Response(serializer.data, status.HTTP_200_OK)
        except StudentClass.DoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            data = request.data
            detail = StudentClass.objects.create(
                student=Student.objects.get(id=data["id"]), bloodGroup = data["bloodGroup"], address = data["address"])
            detail.save()
            serializer = StudentClassSerializer(detail, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        studentClass = StudentClass.objects.get(student=student)
        serializer = StudentClassSerializer(instance=studentClass,data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == 'DELETE':
        return Response('Not allowed by system')

@api_view(['GET', 'POST', 'PUT','DELETE'])
def subject(request):
    sub = request.query_params["subject"]
    stu = request.query_params["student"]
    try:
        student = Student.objects.get(id=stu)
    except Student.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        try:
            subject = Subject.objects.get(student=student)
            serializer = SubjectSerializer(subject, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        except Subject.DoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        try:
            data = request.data
            subject = Subject.objects.create(subject = data["subject"])
            subject.save()
            subject.student.add(student)
            serializer = StudentClassSerializer(subject, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        subject = Subject.objects.get(student=student)
        serializer = StudentClassSerializer(instance=subject,data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == 'DELETE':
        return Response('Not allowed by system')

def test(request):
    return render(request, "test.html")
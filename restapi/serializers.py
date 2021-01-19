from rest_framework import serializers
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", 'phone']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["firstName", 'lastName', 'studentID']


class DetailedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedStudent
        fields = ["id","student","bloodGroup", 'address']


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ["id","student", 'studentClass']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id","student", 'subject']




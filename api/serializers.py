from rest_framework import serializers

from django.contrib.auth.models import Group, User

from .models import Classroom, Test, Question, Choice, TestResult, Score, Homework, ReturnedHomework, DoubtBox

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['classname', 'teacher1', 'teacher2', 'teacher3']


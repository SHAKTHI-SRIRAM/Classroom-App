from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Classroom, Test, Question, Choice
from .serializers import ClassroomSerializer


# @api_view(['POST'])
# @user_passes_test(lambda u: u.is_authenticated)
# @user_passes_test(lambda u: u.is_staff or u.is_superuser)
# def api_classroom_create_view(request):
#     serializer = ClassroomSerializer(data=request.POST)

#     group = Group.objects.create(name=request.POST.classname)
#     user = User.objects.get(username = request.user)
#     user.groups.add(group)

#     if serializer.is_valid(raise_exception=True):
#         classroom = serializer.save()
#         return Response({}, status=201)
#     return Response({}, status=400)


@api_view(['POST'])
def api_classroom_view(request):
    if request.method == "POST":
        if request.user.is_staff():
            data = {
                'classname': request.data.get['classname'],
                'teacher1': request.data.get['teacher1'],
                'teacher2': request.data.get['teacher2'],
                'teacher3': request.data.get['teacher3'],
            }
            serializer = ClassroomSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                group = Group.objects.create(data['classname'])
                user = User.objects.get(username = request.user)
                user.groups.add(group)
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response({"error": "You are not authorized to create a classroom."}, status=403)
    else:
        return Response({"error": "This request method is not allowed"}, status=400)


class ClassroomView(APIView):
    def get(self, request, format=None):
        groups = request.user.groups.all()
        if groups:
            data = {'classrooms': []}
            for group in groups:
                classroom = Classroom.objects.get(classname=group.name)
                class_data = {
                    'classname': classroom.classname,
                    'teacher1': classroom.teacher1,
                    'teacher2': classroom.teacher2,
                    'teacher3': classroom.teacher3,
                }
                data['classrooms'].append(class_data) 
            return Response(data, status=200)
        else:
            data = {
                'message': "You still haven't joined a classroom."
            }
            return Response(data, status=404)

    def post(self, request, format=None):
        if request.user.is_staff:
            serializer = ClassroomSerializer(data=request.data)
            if serializer.is_valid():
                Group.objects.create(name=request.data['classname'])
                group = Group.objects.get(name=request.data['classname'])
                user = User.objects.get(username = request.user)
                user.groups.add(group)
                serializer.save()
                return Response({"message": "The classroom is created"}, status=201)
            return Response({"error": "The classroom cant be created"}, status=400)
        else:
            return Response({"error": "You are not authorized to create a class"}, status=403)
    

# TEACHERS VIEWS


# STUDENTSVIEWS
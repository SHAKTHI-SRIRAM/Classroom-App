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

from .models import Classroom, Test, Question, Choice, Homework
from .serializers import ClassroomSerializer, TestSerializer


class ClassroomView(APIView):
    def get(self, request, format=None):
        groups = request.user.groups.all()
        if groups:
            data = {'classrooms': []}
            data['user'] = request.user.username
            if request.user.is_staff or request.user.is_superuser:
                data['is_teacher'] = True
                data['is_student'] = False
            else:
                data['is_teacher'] = False
                data['is_student'] = True
            for group in groups:
                classroom = Classroom.objects.get(classname=group.name)
                class_data = {
                    'classname': classroom.classname,
                    'teacher1': classroom.teacher1,
                    'teacher2': classroom.teacher2,
                    'teacher3': classroom.teacher3,
                    'class_id': classroom.class_id,
                }
                data['classrooms'].append(class_data) 
            return Response(data, status=200)
        else:
            data = {
                'message': "You still haven't joined a classroom."
            }
            return Response(data, status=200)

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
            return Response({"error": "The classroom cant be created. The details you gave were not proper!"}, status=400)
        else:
            return Response({"error": "You are not authorized to create a class"}, status=403)
    

# TEACHERS VIEWS
class TestView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        groups = request.user.groups.all()
        if groups:
            data = {'tests': []}
            test_title = ""
            for group in groups:
                classroom = Classroom.objects.get(classname=group.name)
                tests = Test.objects.filter(classroom=classroom)
                if tests:
                    for test in tests:
                        questions = Question.objects.filter(test=test)
                        test_data = {
                                'test_title': test.title,
                                'deadline': test.deadline,
                                'qa': [],
                            }
                        for question in questions:
                            choices = Choice.objects.filter(question=question)
                            qa = {
                                'question': question.question,
                                'choices': [],
                            }
                            for choice in choices:
                                choice_dic = {
                                    'choice': choice.choice,
                                    'is_correct': choice.is_correct
                                }
                                qa['choices'].append(choice_dic)
                            test_data['qa'].append(qa)
                            data['tests'].append(test_data)
                    return Response(data, status=200)
                else:
                    return Response({'tests': 'You have no tests available'}, status=200)
        else:
            data = {
                'message': "You still haven't joined a classroom."
            }
            return Response(data, status=404)


class HomeworkView(APIView):
    def get(self, request, format=None, *args, **kwargs):
            if request.user.groups.all():
                data = {'homeworks': []}
                test_title = ""
                groups = request.user.groups.all()
                for group in groups:
                    classroom = Classroom.objects.get(classname=group.name)
                    try:
                        homeworks = Homework.objects.filter(classroom=classroom)
                        for homework in homeworks:
                            hw = {
                                "classroom": homework.classroom.classname,
                                "title": homework.title,
                                "deadline": homework.deadline,
                                "link": f"student/homework/{homework.title.replace(' ', '-')}",
                            }
                            data['homeworks'].append(hw)
                    except Homework.objects.filter(classroom=classroom).DoesNotExist:
                        return Response({'tests': 'You have no homeworks are available'}, status=200)
                return Response(data, status=200)
            else:
                data = {
                    'message': "You still haven't joined a classroom."
                }
                return Response(data, status=404)






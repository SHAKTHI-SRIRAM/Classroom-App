from django.urls import path

from . import views

urlpatterns = [
    path('classrooms/', views.ClassroomView.as_view(), name='api_classroom'),
    path('tests/', views.TestView.as_view(), name='api_test'),
    path('homeworks/', views.HomeworkView.as_view(), name='api_homeworks'),
]

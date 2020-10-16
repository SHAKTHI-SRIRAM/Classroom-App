from django.urls import path

from . import views

urlpatterns = [
    # path('create-classroom/', views.api_classroom_create_view, name='api_classroom_create'),
    path('classroom/', views.ClassroomView.as_view(), name='api_classroom'),
    path('tests/', views.TestView.as_view(), name='api_test'),
    path('homeworks/', views.HomeworkView.as_view(), name='api_homeworks'),
    # path('classrooms/', views.api_classroom_list_view, name='api_classroom_list'),
]
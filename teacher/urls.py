from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_home, name='teacher-home'),
    path('create-classroom/', views.create_classroom, name='create-classroom'),
    path('test-list/<str:classname>', views.test_list_view, name='test-list-view'),
    path('test-create/<str:classname>', views.test_create_view, name='test-create-view'),
    path('test-returned/<str:test_title>', views.test_returned_view, name='test-returned-view'),
    path('homework-create/<str:classname>', views.homework_create_view, name='homework-create-view'),
    path('homework-returned/<str:hw_title>', views.homework_returned_view, name='homework-returned-view'),
    path('test/<str:test_title>', views.test_view, name='test-view'),
    path('add-question/<str:test_title>', views.add_question, name='add-question'),
]
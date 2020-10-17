from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_home, name='student-home'),
    path('join-classroom/', views.join_classroom, name='join-classroom'),
    path('test/<str:test_title>', views.test_view, name='student_test_view'),
    path('test-result/<str:test_title>', views.test_result_view, name='student_test_result_view'),
    path('homework/<str:hw_title>', views.hw_view, name='student_hw_view'),
]
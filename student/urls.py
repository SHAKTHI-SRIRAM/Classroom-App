from django.urls import path
from . import views

urlpatterns = [
    path('test/<str:test_title>', views.test_view, name='student_test_view')
]
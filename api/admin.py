from django.contrib import admin
from .models import Classroom, Test, Question, Choice

# Register your models here.
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['classname', 'teacher1', 'teacher2', 'teacher3']
    search_fields = ['classname']
    class Meta:
        model = Classroom

admin.site.register(Classroom, ClassroomAdmin)


class TestAdmin(admin.ModelAdmin):
    list_display = ['classroom', 'title']
    search_fields = ['title']
    class Meta:
        model = Test

admin.site.register(Test, TestAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['test', 'question']
    search_fields = ['question']
    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice', 'is_correct']
    search_fields = ['choice']
    class Meta:
        model = Choice

admin.site.register(Choice, ChoiceAdmin)
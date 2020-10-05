from django.contrib import admin
from .models import Classroom, Test, Question, Choice, TestResult, Score, Homework, ReturnedHomework, DoubtBox

# Register your models here.
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['classname', 'teacher1', 'teacher2', 'teacher3']
    search_fields = ['classname']
    class Meta:
        model = Classroom

admin.site.register(Classroom, ClassroomAdmin)


class TestAdmin(admin.ModelAdmin):
    list_display = ['classroom', 'title']
    search_fields = ['title', 'classroom__classname']
    class Meta:
        model = Test

admin.site.register(Test, TestAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['test', 'question']
    search_fields = ['question', 'test__title']
    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice', 'is_correct']
    search_fields = ['choice', 'question__question']
    class Meta:
        model = Choice

admin.site.register(Choice, ChoiceAdmin)


class TestResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'test', 'score']
    search_fields = ['student__username', 'test__title']
    class Meta:
        model = TestResult

admin.site.register(TestResult, TestResultAdmin)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['student', 'classroom', 'score']
    search_fields = ['student__username', 'classroom__classname']
    class Meta:
        model = Score

admin.site.register(Score, ScoreAdmin)


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'classroom', 'deadline']
    search_fields = ['title', 'classroom__classname']
    class Meta:
        model = Homework

admin.site.register(Homework, HomeworkAdmin)


class ReturnedHomeworkAdmin(admin.ModelAdmin):
    list_display = ['homework', 'student', 'mark', 'is_returned']
    search_fields = ['homework__title', 'student__username', 'is_returned']
    class Meta:
        model = ReturnedHomework

admin.site.register(ReturnedHomework, ReturnedHomeworkAdmin)


class DoubtBoxAdmin(admin.ModelAdmin):
    list_display = ['user', 'classroom']
    search_fields = ['user__username', 'classroom__classname']
    class Meta:
        model = DoubtBox

admin.site.register(DoubtBox, DoubtBoxAdmin)


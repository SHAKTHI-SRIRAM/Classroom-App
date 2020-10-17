from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Classroom(models.Model):
    classname = models.CharField(max_length=80)
    teacher1 = models.CharField(max_length=30)
    teacher2 = models.CharField(max_length=30, null=True, blank=True)
    teacher3 = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.classname


class Test(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.choice 


class TestResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.student)


class TestAttendedStudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)


class Score(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.student)


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(str(instance.classroom), filename)

class Homework(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300, null=True, blank=True)
    deadline = models.DateTimeField()
    hwfile = models.FileField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return self.title


def returned_hw_directory_path(instance, filename):
    return '{0}/{1}'.format(str(instance.student), filename)

class ReturnedHomework(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    hwfile = models.FileField(upload_to=returned_hw_directory_path)
    mark = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    is_returned = models.BooleanField()

    def __str__(self):
        return str(self.student)


class DoubtBox(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=timezone.now())

    class Meta:
        verbose_name_plural = "Doubt Boxes"

    def __str__(self):
        return str(self.user)

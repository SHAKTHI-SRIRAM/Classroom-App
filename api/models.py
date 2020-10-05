from django.db import models

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



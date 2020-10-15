from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from api.models import Test, Question, Choice

# Create your views here.
@login_required
def test_view(request, test_title):
    if request.method == 'POST':
        score = 0
        for item in request.POST:
            if item != 'csrfmiddlewaretoken' and item != 'action':
                if request.POST[item]:
                    score += 10
        print(score)
        return HttpResponse("It works")
    elif request.method == 'GET':
        data = {
            "classroom": "",
            "deadline": None,
            "title": "", 
            "qa": []
            }
        test = Test.objects.get(title=test_title.replace('-', ' '))
        data['title'] = test.title
        data['classroom'] = test.classroom
        data['deadline'] = test.deadline
        # group = request.user.groups.get(name=test.classroom)
        if request.user.groups.get(name=test.classroom):
            questions = Question.objects.filter(test=test)
            for question in questions:
                choices = Choice.objects.filter(question=question)
                q_a = {
                        'question': question.question,
                        'choices': [],
                    }
                for choice in choices:
                    choice_dic = {
                                    'choice': choice.choice,
                                    'is_correct': choice.is_correct
                                }
                    q_a['choices'].append(choice_dic)
                data['qa'].append(q_a)
            return render(request, 'test.html', data)
        else:
            return HttpResponse("You cannot attend this test")
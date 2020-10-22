from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.utils import timezone

from api.models import (Test, Question, Choice, TestResult, TestAttendedStudent, Homework, ReturnedHomework, Classroom, Score)
from api.forms import ReturnedHomeworkForm


@login_required
def student_home(request):
    user = User.objects.get(username=request.user)
    scores = Score.objects.filter(student=request.user)
    total_score  = 0
    for score in scores:
        total_score += score.score
    data = {
        'user': request.user,
        'score': total_score,
        'classrooms' : []
        }
    try:
        groups = user.groups.all()
        for group in groups:
            classroom = Classroom.objects.get(classname=group.name)
            userscore = Score.objects.get(student=request.user, classroom=classroom)
            user_score = userscore.score
            clsrm = {
                'classname': classroom.classname,
                'teacher1': classroom.teacher1,
                'teacher2': classroom.teacher2,
                'teacher3': classroom.teacher3,
                'pk': classroom.pk,
                'your_score': 0,
                'no_of_tests': 0,
                'no_of_homeworks': 0,
                'tests': [],
                'homeworks': [],
                }
            clsrm['your_score'] = user_score
            try:
                tests = Test.objects.filter(classroom=classroom)
                no_of_tests = len(tests)
                clsrm['no_of_tests'] = no_of_tests
                for test in tests:
                    link = test.title.replace(' ', '-')
                    _test_ = {
                        'test_title': test.title,
                        'test_link': f'test/{link}',
                        'deadline': test.deadline,
                        }
                    clsrm['tests'].append(_test_)
            except:
                pass

            try:
                homeworks = Homework.objects.filter(classroom=classroom)
                no_of_homeworks = len(homeworks)
                clsrm['no_of_homeworks'] = no_of_homeworks

                for homework in homeworks:
                    link = homework.title.replace(' ', '-')
                    _homework_ = {
                        'homework_title': homework.title,
                        'homework_link': f'homework/{link}',
                        'deadline': homework.deadline,
                    }
                    clsrm['homeworks'].append(_homework_)
                
            except:
                pass
            data['classrooms'].append(clsrm)
        return render(request, 'student-home.html', data)

    except:
        return render(request, 'student-home.html', {"message": "You haven't joined a class yet"})


@login_required
def join_classroom(request):
    if request.method == 'GET':
        return render(request, 'join-classroom.html')

    elif request.method == 'POST':
        class_id = int(request.POST.get('class_id'))
        try:
            classroom = Classroom.objects.get(class_id=class_id)
            user = User.objects.get(username=request.user)
            group = Group.objects.get(name=classroom.classname)
            if user.is_staff or user.is_superuser:
                if group in user.groups.all():
                    return redirect('teacher-home')
                else:
                    user.groups.add(group)
                    return redirect('teacher-home')
            else:
                if group in user.groups.all():
                    score = Score.objects.get(classroom=classroom, student=user)
                    score.save()
                    return redirect('student-home')
                else:
                    score = Score.objects.create(classroom=classroom, student=user, score=0)
                    score.save()
                    user.groups.add(group)
                    return redirect('student-home')

        except:
            data = {"message": "The Class ID you have entered is invalid."}
            return render(request, 'join-classroom.html', data)


@login_required
def test_view(request, test_title):

    if request.method == 'POST':
        score = 0
        for item in request.POST:
            if item != 'csrfmiddlewaretoken' and item != 'action':
                if request.POST[item] == "True":
                    score += 10

        student = User.objects.get(username=request.user)
        test = Test.objects.filter(title=test_title.replace('-', ' ')).last()
        if test.deadline > timezone.now():
            classroom = test.classroom
            user = User.objects.get(username=request.user)

            user_score = Score.objects.get_or_create(student=user, classroom=classroom)
            user_score_score = user_score[0].score
            if user_score[0].score:
                new_score = user_score_score + score
                score_ = Score.objects.get(student=user, classroom=classroom)
                score_.score = new_score
                score_.save()
            else:
                new_score = score
                score_ = Score.objects.get(student=user, classroom=classroom)
                score_.score = new_score
                score_.save()

            TestAttendedStudent.objects.get_or_create(test=test, student=student)
            test_result = TestResult.objects.get_or_create(student=student, test=test)
            test_result = TestResult.objects.get_or_create(student=student, test=test)
            test_result[0].score = score
            test_result[0].save()
            return redirect("student_test_result_view", test_title=test_title)
        else:
            return HttpResponse("<h1>You have exceeded the timelimit of the test.</h1>")

    elif request.method == 'GET':
        data = {
            "classroom": "",
            "deadline": None,
            "title": "", 
            "qa": []
            }
        test = Test.objects.filter(title=test_title.replace('-', ' ')).last()
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


@login_required
def test_result_view(request, test_title):

    test = Test.objects.filter(title=test_title.replace('-', ' ')).last()
    no_of_qs = Question.objects.filter(test=test).count()
    user = User.objects.get(username=request.user)
    if TestAttendedStudent.objects.filter(test=test, student=user):
        
        test_result = TestResult.objects.get(test=test, student=user)
        data = {
            "test_title": test_result.test.title,
            "student": test_result.student.username,
            "score": test_result.score,
            "total": no_of_qs * 10,
            "title": "Test Result",
        }
        return render(request, 'student-test-result.html', data)
    else:
        data = {
            "message": "You still havent attended this test!!..",
            "test_link": f"test/{test.title.replace('-', ' ')}",
        }
        return render(request, 'student-test-result.html', data)

    return render('Itworks')


@login_required
def hw_view(request, hw_title):
    if request.method == 'GET':
        try:
            homework = Homework.objects.get(title=hw_title.replace('-', ' '))
            try:
                hw_path = homework.hwfile.path
                path_list = hw_path.rpartition('\\')
                hw_pa = homework.classroom.classname.replace(' ', '%20')
                link = f'/media/{hw_pa}/{path_list[-1]}'
            except:
                link = None
            data = {	          
                "classroom": homework.classroom.classname,
                "title": homework.title,	                   
                "deadline": homework.deadline,	                    
                "desc": homework.desc,	                                       
                "form": ReturnedHomeworkForm(),
            }
            data['hwfile'] = link       
            return render(request, 'student-hw-view.html', data)	           
        except:
            data = {"message": "The homework you are asking is not available!!.."}
            return render(request, 'student-hw-view.html', data)
    
    elif request.method == 'POST':
        form = ReturnedHomeworkForm(request.POST, request.FILES)
        if form.is_valid():
            hwfile = request.FILES['hwfile']
            student = User.objects.get(username=request.user)
            homework = Homework.objects.get(title=hw_title.replace('-', ' '))
            ReturnedHomework.objects.get_or_create(hwfile=hwfile, student=student, homework=homework, is_returned=True)
            return redirect('home')
        else:
            try:
                homework = Homework.objects.get(title=hw_title.replace('-', ' '))
                hw_path = homework.hwfile.path
                path_list = hw_path.rpartition('\\')
                hw_pa = homework.classroom.classname.replace(' ', '%20')
                link = f'/media/{hw_pa}/{path_list[-1]}'
                data = {
                    "message": "Your homework was not valid",
                    "classroom": homework.classroom.classname,
                    "title": homework.title,
                    "deadline": homework.deadline,
                    "desc": homework.desc,
                    "hwfile": link,
                    "form": ReturnHomeworkForm()
                }
            except:
                data = {"message": "The homework you are asking is not available!!.."}
            return render(request, 'student-hw-view.html', data)



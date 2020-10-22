from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from api.models import (Test, Question, Choice, TestResult, TestAttendedStudent, Homework, ReturnedHomework, Classroom, Score)


@login_required
def teacher_home(request):
    if request.user.is_staff or request.user.is_superuser:
        user = User.objects.get(username=request.user)
        data = {
            "user": request.user,
            "classrooms": [],
        }
        try:
            groups = user.groups.all()
            for group in groups:
                classroom = Classroom.objects.get(classname=group.name)
                clsrm = {
                    'classname': classroom.classname,
                    'teacher1': classroom.teacher1,
                    'teacher2': classroom.teacher2,
                    'teacher3': classroom.teacher3,
                    'pk': classroom.pk,
                    'class_id': classroom.class_id,
                    'no_of_tests': 0,
                    'no_of_homeworks': 0,
                    'tests': [],
                    'homeworks': [],
                }

                try:
                    tests = Test.objects.filter(classroom=classroom)
                    no_of_tests = len(tests)
                    clsrm['no_of_tests'] = no_of_tests
                    for test in tests:
                        link = test.title.replace(' ', '-')
                        _test_ = {
                            'test_title': test.title,
                            'test_link': f'test-returned/{link}',
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
                            'homework_link': f'homework-returned/{link}',
                            'deadline': homework.deadline,
                        }
                        clsrm['homeworks'].append(_homework_)
                except:
                    pass
                data['classrooms'].append(clsrm)
            return render(request, 'teacher-home.html', data)
        except:
            return render(request, 'teacher-home.html', {"message": "You haven't joined a class yet."})
        return render(request, 'teacher-home.html')
    else:
        return HttpResponse('''
        You are not authenticated to view this page. Please contact the admin to get staff status.''')


@login_required
def create_classroom(request):
    if request.method == 'GET':
        if request.user.is_staff or request.user.is_superuser:
            return render(request, 'create-classroom.html')
        else:
            return HttpResponse('''
            You are not authenticated to view this page. Please contact the admin to get staff status.''')

    elif request.method == 'POST':
        if request.user.is_staff or request.user.is_superuser:
            user = User.objects.get(username=request.user)
            data = request.POST
            classname = data['classname']
            teacher1 = data['teacher1']
            teacher2 = data['teacher2']
            teacher3 = data['teacher3']
            Classroom.objects.create(classname=classname, teacher1=teacher1, teacher2=teacher2, teacher3=teacher3)
            classroom = Classroom.objects.get(classname=classname)
            pk = classroom.pk
            classroom.class_id = 100000 + pk
            classroom.save()
            group = Group.objects.create(name=classname)
            user.groups.add(group)
            return redirect('teacher-home')
        else:
            return HttpResponse('''
            You are not authenticated to view this page. Please contact the admin to get staff status.''')


@login_required
def test_list_view(request, classname):
    if request.method == 'GET':
        user = User.objects.get(username=request.user)
        classname = classname.replace('-', ' ')
        classroom = Classroom.objects.get(classname=classname)
        data = {
            "classroom": classname,
            "tests": [],
        }
        tests = Test.objects.filter(classroom=classroom)
        for test in tests:
            link = test.title.replace(' ', '-')
            _test_ = {
                'test_title': test.title,
                'test_link': f'/teacher/test/{link}',
                'deadline': test.deadline,
                }
            data['tests'].append(_test_)
        return render(request, 'test-list-view.html', data)


@login_required
def test_view(request, test_title):
    if request.method == 'GET':
        if request.user.is_staff or request.user.is_superuser:
            user = User.objects.get(username=request.user)
            test = Test.objects.get(title = test_title.replace('-', ' '))
            questions = Question.objects.filter(test=test)
            no_of_questions = len(questions)
            data = {
                "test_title": test.title,
                "classroom": test.classroom,
                "deadline": test.deadline,
                "no_of_questions": no_of_questions,
                "qa": []
            }
            for question in questions:
                q_a = {
                    "q": question.question,
                    "choices": [],
                }
                choices = Choice.objects.filter(question=question)
                for choice in choices:
                    _choice_ = {
                        "choice": choice.choice,
                        "is_correct": choice.is_correct
                    }
                    q_a['choices'].append(_choice_)
                data['qa'].append(q_a)
            return render(request, 'teacher-test-view.html', data)

        else:
            return HttpResponse('''You are not authenticated to view this page. Please contact the admin to get staff status''')


@login_required
def test_create_view(request, classname):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'GET':
            return render(request, 'test-create.html')

        elif request.method == 'POST':
            classroom = Classroom.objects.get(classname=classname.replace('-', ' '))
            title = request.POST['test_title']
            deadline = request.POST['deadline']
            Test.objects.create(classroom=classroom, title=title, deadline=deadline)
            test = Test.objects.filter(title=title, classroom=classroom).last()
            link = test.title.replace(' ', '-')
            redirect_link = f'/teacher/add-question/{link}'
            return redirect(redirect_link)
    
    else:
        return HttpResponse('''
        You are not authenticated to view this page. Please contact the admin to get staff status.''')


@login_required
def add_question(request, test_title):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'GET':
            test = Test.objects.filter(title=test_title.replace('-', ' ')).last()
            data = {
                "title": test.title,
                "deadline": test.deadline,
                "classroom": test.classroom,
                "qa": [],
            }
            try:
                questions = Question.objects.filter(test=test)
                for question in questions:
                    q_a = {
                        "q": question.question,
                        "choices": [],
                    }
                    choices = Choice.objects.filter(question=question)
                    for choice in choices:
                        _choice_ = {
                            "choice": choice.choice,
                            "is_correct": choice.is_correct,
                        }
                        q_a['choices'].append(_choice_)
                    data['qa'].append(q_a)
                return render(request, 'add-question.html', data)
            except:
                return render(request, 'add-question.html', {"message": "No questions are created yet!"})

        elif request.method == 'POST':
            data = request.POST
            question = data['question']
            test = Test.objects.filter(title=test_title.replace('-', ' ')).last()
            q = Question.objects.create(question=question, test=test)
            correct_choice = data['correct-choice']
            c_choice = data[correct_choice]
            if data['choice1'] != '':
                if data['choice1'] == c_choice:
                    Choice.objects.create(question=q, choice=data['choice1'], is_correct=True)
                else:
                    Choice.objects.create(question=q, choice=data['choice1'], is_correct=False)
            if data['choice2'] != '':
                if data['choice2'] == c_choice:
                    Choice.objects.create(question=q, choice=data['choice2'], is_correct=True)
                else:
                    Choice.objects.create(question=q, choice=data['choice2'], is_correct=False)
            if data['choice3'] != '':
                if data['choice3'] == c_choice:
                    Choice.objects.create(question=q, choice=data['choice3'], is_correct=True)
                else:
                    Choice.objects.create(question=q, choice=data['choice3'], is_correct=False)
            if data['choice4'] != '':
                if data['choice4'] == c_choice:
                    Choice.objects.create(question=q, choice=data['choice4'], is_correct=True)
                else:
                    Choice.objects.create(question=q, choice=data['choice4'], is_correct=False)
            redirect_link = f'/teacher/add-question/{test_title}'
            return redirect(redirect_link)

    else:
        return HttpResponse('''
        You are not authenticated to view this page. Please contact the admin to get staff status.''')


@login_required
def homework_create_view(request, classname):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'GET':
            return render(request, 'hw-create.html')

        elif request.method == 'POST':
            classroom = Classroom.objects.get(classname=classname.replace('-', ' '))
            title = request.POST['title']
            deadline = request.POST['deadline']
            hwfile = request.FILES['hwfile']
            desc = ''
            if request.POST['desc'] != '':
                desc = request.POST['desc']
            Homework.objects.create(classroom=classroom, title=title, desc=desc, deadline=deadline, hwfile=hwfile)
            return redirect('/teacher')
    else:
        return HttpResponse('''
        You are not authenticated to view this page. Please contact the admin to get staff status.''')


@login_required
def test_returned_view(request, test_title):
    if request.user.is_staff or request.user.is_superuser:
        title = test_title.replace('-', ' ')
        test = Test.objects.filter(title=title).last()
        returned_tests = TestResult.objects.filter(test=test)
        data = {
            "classroom": test.classroom,
            "title": title,
            "returned_tests": returned_tests,
        }
        return render(request, 'test-result.html', data)
    else:
        return HttpResponse('''
        You are not authenticated to view this page. Please contact the admin to get staff status.''')


@login_required
def homework_returned_view(request, hw_title):
    if request.user.is_staff or request.user.is_superuser:
        title = hw_title.replace('-', ' ')
        homework = Homework.objects.get(title=title)
        returned_hws = ReturnedHomework.objects.filter(homework=homework)
        data = {
            "classroom": homework.classroom,
            "title": title,
            "returned_hws": []
        }
        for hw in returned_hws:
            h_w = {
                "student": hw.student,
                "is_returned": hw.is_returned,
            }
            hw_path = hw.hwfile.path
            path_list = hw_path.rpartition('\\')
            hw_pa = homework.classroom.classname.replace(' ', '%20')
            link = f'/media/{hw.student}/{path_list[-1]}'
            h_w['hwfile'] = link
            data['returned_hws'].append(h_w)
        return render(request, 'hw-result.html', data)
    else:
        return HttpResponse('''
        You are not authenticated to view this page. Please contact the admin to get staff status.''')
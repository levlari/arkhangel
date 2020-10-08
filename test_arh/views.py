from django.shortcuts import render,get_object_or_404, redirect
from .models import Question, Answers

#user_answers = []
#user_points = 0

def test_arh(request):

    if request.user.username == 'AnonymousUser':  return redirect('')
    question_ids = Question.objects.all().values_list('id', 'body', 'title') #,'answers', 'body', 'title')
    if request.user.curent_question > len(question_ids):
        return redirect('/final/' )
    print('question_id = '+str(request.user.curent_question))
    print ('question_len = ' + str(len(question_ids)))
    question =  get_object_or_404(Question, id = request.user.curent_question)
    answers = question.answers.filter(active=True)
    correct_answer = answers.filter(correct_answer=True)
    print('correct_answer is ' + str(correct_answer[0]))

    if request.method == 'POST':

        try:
            request.user.answers+=str(request.POST['radio'])
        except:
            return render(request,
                          'test_arh/question.html',
                          {'question': question,
                           'answers': answers,
                           })

        request.user.curent_question += 1

        print('radio is ' + str(request.POST['radio']))
        if str(request.POST['radio']) == str(correct_answer[0]):

            request.user.points += 1# прибавляем счётчик правильных ответов




    print('correct_answer is '+ str(correct_answer[0]))

    request.user.save()
    if request.user.curent_question > len(question_ids):
        return redirect('/final/' )
    print('question_id = '+str(request.user.curent_question))
    print ('question_len = ' + str(len(question_ids)))
    question =  get_object_or_404(Question, id = request.user.curent_question)
    answers = question.answers.filter(active=True)
    return render(request,
                  'test_arh/question.html',
                  {'question': question,
                   'answers': answers,
                   }
)

def test_arh_final (request):
    if request.user.username == 'AnonymousUser':  return redirect('/')


    return render(request,
                  'test_arh/final.html',
                  {'points': request.user.points,
                   'answers': request.user.answers,
                   'username': request.user.username,
                   }
                  )

def test_arh_start (request):
    return render(request,
                  'test_arh/start.html',)
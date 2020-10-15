from django.shortcuts import render,get_object_or_404, redirect
from .models import Question, Answers
import datetime

#user_answers = []
#user_points = 0

def test_arh(request):
    if request.method == 'GET' and request.user.curent_question == 1:
        request.user.time_begin = datetime.datetime.now().time()
    if request.user.username == 'AnonymousUser':  return redirect('')
    question_ids = Question.objects.all().values_list('id', 'body', 'title','test_id') #,'answers', 'body', 'title')
    question_ids = question_ids.filter(test_id = request.user.curent_test)
#    print (question_ids.all())
    if request.user.curent_question > len(question_ids) or (timeinsec(request.user.time_begin)+10*60) < timeinsec(datetime.datetime.now().time()):
        request.user.curent_question = len(question_ids) +1
        request.user.save()
        return redirect('/final/' )
#    print('question_id = '+str(request.user.curent_question))
#    print ('question_len = ' + str(len(question_ids)))
    question =  get_object_or_404(Question, Num = request.user.curent_question, test_id = request.user.curent_test)
    time_to_live = timeintime (timeinsec(request.user.time_begin)+15*60 -timeinsec(datetime.datetime.now().time()))
    answers = question.answers.filter(active=True)
    correct_answer = answers.filter(correct_answer=True)


    if request.method == 'POST':

        try:
            request.user.answers+=str(request.POST['radio']) + '; '
        except:
            return render(request,
                          'test_arh/question.html',
                          {'question': question,
                           'answers': answers,
                           })

        request.user.curent_question += 1



        if str(request.POST['radio']) == str(correct_answer[0]):

            request.user.points += 1# прибавляем счётчик правильных ответов




#    print('correct_answer is '+ str(correct_answer[0]))

    request.user.save()
    if request.user.curent_question > len(question_ids):
        return redirect('/final/' )
#    print('question_id = '+str(request.user.curent_question))
#    print ('question_len = ' + str(len(question_ids)))
    question =  get_object_or_404(Question, Num = request.user.curent_question, test_id = request.user.curent_test)
    answers = question.answers.filter(active=True)
    return render(request,
                  'test_arh/question.html',
                  {'question': question,
                   'answers': answers,
                   'time_to_live' : time_to_live,
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

def timeinsec (intime: datetime.time):
    return intime.hour * 60 * 60 + intime.minute * 60 + intime.second

def timeintime (inseconds: int):

    return datetime.time(hour = inseconds // (60*60), minute= (inseconds % (60*60)) // 60, second= (inseconds % (60*60)) % 60 )
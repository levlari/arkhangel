from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Test
from django.core.exceptions import ObjectDoesNotExist
import datetime
from users.models import CustomUser


DEFAULT_TIMETOTEST = '00:15:00'


def testing(request):
    # проверяем запрос на начало теста
    if request.method == 'GET' and request.user.curent_question == 1:  # если 1 вопрос
        request.user.time_begin = datetime.datetime.now().time()  # засекаем время
        request.user.date_begin = datetime.date.today()  # и дату
        request.user.save()  # сохраняем
    if request.user.username == 'AnonymousUser':
        return redirect('')

    # получаем набор вопросов для теста пользователя, время на этот тест
    question_ids = Question.objects.all().values_list('id', 'body', 'title', 'test_id')
    print(request.user.curent_question, question_ids)
    question_ids = question_ids.filter(test_id=request.user.curent_test)
    print('question_ids',request.user.curent_test, question_ids.all(), Question.objects.all())
    cur_test = Test.objects.get(test_id=request.user.curent_test)
    timetotest = cur_test.TimeToTest
    # проверяем на законченность тест по вопросам или по времени,
    # переведя в секунды время начала и время на тест, текущую дату
    # учитываем смену дня
    cur_time_in_sec = timeinsec(datetime.datetime.now().time())
    if request.user.date_begin < datetime.date.today():
        cur_time_in_sec = cur_time_in_sec + 86400*(datetime.date.today() - request.user.date_begin).days

    if request.user.curent_question > len(question_ids) or (
            timeinsec(request.user.time_begin) + timeinsec(timetotest)) < cur_time_in_sec:
        # увеличиваем счётчик вопросов, и выходим на конечную страницу
        print('/final/',request.user.curent_question, len(question_ids))
        print(question_ids)
        request.user.curent_question = len(question_ids) + 1
        request.user.save()
        return redirect('/final/')

    # получаем объект текущего вопроса,
    # на основе поля curent_question у запрошенного пользователя
    # и его номера теста
    question = get_object_or_404(Question, Num=request.user.curent_question, test_id=request.user.curent_test)
    # получаем время до конца в формате времени,
    # а вычисляем время в секундах: (время от начала + время на тест) - текущее время
    time_to_live = timeintime(timeinsec(request.user.time_begin) +
                              timeinsec(timetotest) - cur_time_in_sec)
    # получаем набор активных ответов и правильный ответ
    answers = question.answers.filter(active=True)
    correct_answer = answers.filter(correct_answer=True)
    # если пользователь отправил пост(ответил на вопрос),
    # то пробуем записать в ответы пользователя выставленый radio_button,
    # увеличиваем указаель на следующий вопрос,
    # или вернем текущий вопрос с ответами
    if request.method == 'POST':
        try:
            request.user.answers += str(request.POST['radio']) + '; '
        except Exception:
            return render(request,
                          'test_arh/question.html',
                          {'question': question,
                           'answers': answers,
                           })
        request.user.curent_question += 1
        # если радио равен правильному ответу
        if str(request.POST['radio']) == str(correct_answer[0]):
            request.user.points += 1  # прибавляем счётчик правильных ответов
        request.user.save()

    # если ответили на последний вопрос, возвращаем конечную страницу
    if request.user.curent_question > len(question_ids):
        return redirect('/final/')

    # получаем вопрос и набор ответов
    question = get_object_or_404(Question, Num=request.user.curent_question,
                                 test_id=request.user.curent_test)
    answers = question.answers.filter(active=True)

    # возвращаем страницу шаблона,
    # текущий вопрос, ответы
    # и оставшееся время на тест
    return render(request, 'test_arh/question.html', {
        'question': question,
        'answers': answers,
        'time_to_live': time_to_live,
        })


# запрос финальной страницы
def test_arh_final(request):
    # в корень неавторизовавшихся
    if request.user.username == 'AnonymousUser':
        return redirect('/')
    # выводим результаты теста
    return render(request, 'test_arh/final.html', {
        'points': request.user.points,
        'answers': request.user.answers,
        'username': request.user.username,
        })


# открыть стартовую страницу
def test_arh_start(request):
    Test_obj = Test.objects.all()
    message = ''
    if not Test_obj:
        default_test = Test()
        default_test.TimeToTest = DEFAULT_TIMETOTEST
        default_test.save()
        message = 'Default test created'
        print(message)
        try:
            admin_user = CustomUser.object.get(username='admin')
            admin_user.curent_test = 1
            admin_user.save()
        except ObjectDoesNotExist:
            pass
    if message != '':
        return render(request, 'test_arh/start.html',{'message':message} )
    else:
        return render(request, 'test_arh/start.html',)



# перевод времени из формата(чч:мм:сс) в секунды(число)
def timeinsec(intime: datetime.time):
    return intime.hour * 60 * 60 + intime.minute * 60 + intime.second


# перевод времени из секунд(число) в формат(чч:мм:сс)
def timeintime(inseconds: int):
    return datetime.time(hour=inseconds // (60 * 60), minute=(inseconds % (60 * 60)) // 60,
                         second=(inseconds % (60 * 60)) % 60)

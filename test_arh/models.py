from django.db import models


class Test(models.Model):
    objects = models.Manager()
    test_id = models.IntegerField(default=1)
    TimeToTest = models.TimeField()

    def __int__(self):
        return self.test_id

    def __str__(self):
        return str(self.test_id)


class Question(models.Model):
    objects = models.Manager()  # Менеджер по умолчанию.
    test_id = models.ForeignKey(Test,
                                on_delete=models.CASCADE,
                                related_name='question')
    Num = models.IntegerField(default=1)
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return str(self.test_id) + ' - ' + str(self.Num)+'  ' + self.body


class Answers(models.Model):
    objects = models.Manager()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='answers')
    name = models.CharField(max_length=80)
    body = models.TextField()
    active = models.BooleanField(default=True)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.body


# class users_Answer(models.Model):
#     given_answer = models.TextField()
#     body = models.TextField()
#     active = models.BooleanField(default=True)
#     correct_answer = models.BooleanField(default=False)

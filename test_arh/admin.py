from django.contrib import admin
from .models import Question, Answers, Test


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'Num', 'test_id')
    search_fields = ('title', 'body')


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('name',  'body', 'active', 'correct_answer', 'question')
    list_filter = ('active', 'correct_answer', 'question')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test_id',  'TimeToTest')

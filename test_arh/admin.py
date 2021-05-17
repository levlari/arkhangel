from django.contrib import admin
from .models import Question, Answers, Test

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','body', 'Num', 'test_id')
    #list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ('status', 'publish')
@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('name',  'body', 'active', 'correct_answer','question')
    list_filter = ('active', 'correct_answer', 'question')
   # search_fields = ('name',  'body','question')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test_id',  'TimeToTest')
#    list_filter = ('test_id')
 #   search_fields = ('test_id')
# Register your models here.

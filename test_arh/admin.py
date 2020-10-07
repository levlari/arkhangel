from django.contrib import admin
from .models import Question, Answers

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','body')
    #list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ('status', 'publish')
@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('name',  'body', 'active', 'correct_answer','question')
    list_filter = ('active', 'correct_answer')
    search_fields = ('name',  'body')

# Register your models here.

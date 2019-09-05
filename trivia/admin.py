from django.contrib import admin

from .models import Question, Answer, Category, Quiz
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    max_num = 8


class QuestionAdmin(admin.ModelAdmin):

    fields = ['question', 'quiz']
    inlines = [AnswerInline]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["category", ]


class QuestionInline(admin.TabularInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    fields = ['name', 'category']
    inlines = [QuestionInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)

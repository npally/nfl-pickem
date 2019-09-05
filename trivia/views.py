from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Quiz, Answer
from django import forms
from .forms import QuizForm
from django.core.exceptions import ValidationError

# Create your views here.


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'


class QuizResultsView(DetailView):
    model = Quiz
    template_name = 'results.html'


def quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.question_set.all()

    total_questions = 0
    correct_answers = 0

    if request.method == 'POST':

        for question in questions:
            q = "answer" + str(question.id)

            if q not in request.POST:
                return HttpResponse("Please go back and answer all questions.")

            selected_choice = question.answer_set.get(
                pk=request.POST[q])

            if selected_choice.correct == True:
                correct_answers += 1
                total_questions += 1
            else:
                total_questions += 1

            context = {'correct_answers': correct_answers,
                       'total_questions': total_questions}

        return render(request, 'results.html', context)

    else:
        return render(request, 'quiz_detail.html', {'questions': questions})

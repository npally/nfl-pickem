from django.db import models

from django.urls import reverse

import random
# Create your models here.


class Quiz(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    question = models.CharField(max_length=150)
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('quiz_detail', args=[str(self.id)])

    def get_answers(self):
        answers = sorted(self.answer_set.all(), key=lambda x: random.random())

        return answers

    # def check_answer(self, answer):
    #   return self.answer_set.filter(id=answer.id, correct=True).exists()

    # def get_correct_answer(self):
        # return self.answer_set.filter(correct=True)


class Answer(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, blank=False)
    correct = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.answer

    def get_absolute_url(self):
        return reverse('quiz_list')


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'

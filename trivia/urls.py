from django.urls import path

from .views import QuizListView, QuizResultsView
from .import views

urlpatterns = [
    path("", QuizListView.as_view(), name='quiz_list'),
    path("<int:pk>/", views.quiz, name='quiz_detail'),
    path("<int:pk>/results/", QuizResultsView.as_view(), name='results')
]

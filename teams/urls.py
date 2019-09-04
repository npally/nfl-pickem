from django.urls import path

from .views import HomePageView, TeamCreateView, TeamListView, TeamDetailView, RulesPageView, PowerRankingView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('newteam/', TeamCreateView.as_view(), name='new-team'),
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('rules/', RulesPageView.as_view(), name='rules'),
    path('power-rankings', PowerRankingView.as_view(), name='power-rankings')
]

from django.urls import path

from .views import HomePageView, TeamCreateView, TeamListView, TeamDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('newteam/', TeamCreateView.as_view(), name='new-team'),
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail')
]

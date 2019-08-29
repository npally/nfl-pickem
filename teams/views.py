from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin

from .models import Team
# Create your views here.


class HomePageView(ListView):
    model = Team
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        ordered_teams = sorted(
            Team.objects.all(), key=lambda x: int(x.get_wins()), reverse=True)
        context['ranked_teams'] = ordered_teams
        return context

class RulesPageView(TemplateView):
    template_name = 'rules.html'


class TeamCreateView(CreateView):
    model = Team
    template_name = 'team_new.html'
    fields = ['manager', 'team1', 'team2', 'team3', 'team4']


class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'

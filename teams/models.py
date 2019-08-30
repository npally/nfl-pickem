from django.db import models
from django.core.exceptions import ValidationError
import csv


# Create your models here.
TEAM_CHOICES = [('ARI', 'Arizona Cardinals'), ('ATL', 'Atlanta Falcons'),
                ('BAL', 'Baltimore Ravens'), ('BUF',
                                              'Buffalo Bills'), ('CAR', 'Carolina Panthers'),
                ('CHI', 'Chicago Bears'), ('CIN',
                                           'Cincinnati Bengals'), ('CLE', 'Cleveland Browns'),
                ('DAL', 'Dallas Cowboys'), ('DEN', 'Denver Broncos'), ('DET',
                                                                       'Detroit Lions'), ('GB', 'Green Bay Packers'),
                ('HOU', 'Houston Texans'), ('IND',
                                            'Indianapolis Colts'), ('JAX', 'Jacksonville Jaguars'),
                ('KC', 'Kansas City Chiefs'), ('MIA',
                                               'Miami Dolphins'), ('MIN', 'Minnesota Vikings'),
                ('NE', 'New England Patriots'), ('NO:',
                                                 'New Orleans Saints'), ('NYG', 'New York Giants'),
                ('NYJ', 'New York Jets'), ('OAK',
                                           'Oakland Raiders'), ('PHI', 'Philadelphia Eagles'),
                ('PIT', 'Pittsburgh Steelers'), ('SD:',
                                                 'San Diego Chargers'), ('SEA', 'Seattle Seahawks'),
                ('SF', 'San Francisco 49ers'), ('STL',
                                                'Saint Louis Rams'), ('TB', 'Tampa Bay Buccaneers'),
                ('TEN', 'Tennessee Titans'), ('WAS', 'Washington Redskins')]


class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_name(self):
        return self.first_name + " " + self.last_name


class Team(models.Model):
    manager = models.OneToOneField(
        'Manager', on_delete=models.CASCADE)
    team1 = models.CharField(
        max_length=3, choices=TEAM_CHOICES, blank=True)
    team2 = models.CharField(
        max_length=3, choices=TEAM_CHOICES, blank=True)
    team3 = models.CharField(
        max_length=3, choices=TEAM_CHOICES, blank=True)
    team4 = models.CharField(
        max_length=3, choices=TEAM_CHOICES, blank=True)

    class Meta:
        ordering = ["manager__last_name"]

    def get_teams(self):
        teams = [self.team1, self.team2, self.team3, self.team4]
        return teams

    def __str__(self):
        return self.manager.get_name()

    def get_absolute_url(self):
        return reverse('team-list')

    def clean(self):
        """
        raise error if there are over 8 teams in the league
        """
        model = self.__class__
        if model.objects.count() > 8:
            raise ValidationError("There can only be 8 Teams in a league")

    # deployment file path: '/home/kilgoretrout1/nfl-pickem/records.csv'

    def get_wins(self):
        teams = self.get_teams()

        with open('records.csv') as file:
            csv_reader = csv.DictReader(file)
            w = 0

            for row in csv_reader:
                for team in teams:
                    if row["Abb"] == team:
                        w += int(row['W'])

        return "{}".format(w)

    def get_losses(self):
        teams = self.get_teams()

        with open('records.csv') as file:
            csv_reader = csv.DictReader(file)
            l = 0

            for row in csv_reader:
                for team in teams:
                    if row["Abb"] == team:
                        l += int(row['L'])

        return "{}".format(l)

    def get_ties(self):
        teams = self.get_teams()

        with open('records.csv') as file:
            csv_reader = csv.DictReader(file)
            t = 0

            for row in csv_reader:
                for team in teams:
                    if row["Abb"] == team:
                        t += int(row['T'])

        return "{}".format(t)

    def get_pointsfor(self):
        teams = self.get_teams()

        with open('records.csv') as file:
            csv_reader = csv.DictReader(file)
            pf = 0

            for row in csv_reader:
                for team in teams:
                    if row["Abb"] == team:
                        pf += int(row['PF'])
        return "{}".format(pf)

    def get_winning_percentage(self):
        teams = self.get_teams()

        with open('records.csv') as file:
            csv_reader = csv.DictReader(file)
            wp = 0

            for row in csv_reader:
                for team in teams:
                    if row["Abb"] == team:
                        wp += float(row['WP'])
            wp = int(wp / 4 * 100)
        return "{}%".format(wp)

        def get_pointsfor(self):
            teams = self.get_teams()

            with open('records.csv') as file:
                csv_reader = csv.DictReader(file)
                pf = 0

                for row in csv_reader:
                    for team in teams:
                        if row["Abb"] == team:
                            pf += int(row['PF'])
            return "{}".format(pf)

from django.db import models
from django.core.exceptions import ValidationError
import csv

# deployment file path: '/home/kilgoretrout1/nfl-pickem/records.csv'
CSV_FILE = 'records.csv'

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
                ('NE', 'New England Patriots'), ('NO',
                                                 'New Orleans Saints'), ('NYG', 'New York Giants'),
                ('NYJ', 'New York Jets'), ('OAK',
                                           'Oakland Raiders'), ('PHI', 'Philadelphia Eagles'),
                ('PIT', 'Pittsburgh Steelers'), ('LAC',
                                                 'Los Angeles Chargers'), ('SEA', 'Seattle Seahawks'),
                ('SF', 'San Francisco 49ers'), ('LAR',
                                                'Los Angeles Rams'), ('TB', 'Tampa Bay Buccaneers'),
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

    def get_indv_team_data(self):

        nl = []

        teams = self.get_teams()

        with open(CSV_FILE) as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                for team in teams:
                    if row["abb"] == team:
                        ol = []
                        verbose_name = row["team_name"]

                        w = int(row['wins'])
                        l = int(row['losses'])
                        t = int(row['ties'])

                        record = "{}-{}-{}".format(w, l, t)

                        pf = row['points_for']

                        if pf == "":
                            pf = 0
                        ol.append(verbose_name)
                        ol.append(record)
                        ol.append(pf)
                        nl.append(ol)
        return nl

    def team_records(self):
        nl = []
        teams = self.get_teams()

        with open(CSV_FILE) as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                for team in teams:
                    if row["abb"] == team:
                        w = int(row['wins'])
                        l = int(row['losses'])
                        t = int(row['ties'])
                        record = "{}-{}-{}".format(w, l, t)
                        nl.append(record)
        return nl

    def __str__(self):
        return self.manager.get_name()

    def get_absolute_url(self):
        return reverse('team-list')

    def get_wins(self):
        teams = self.get_teams()

        with open(CSV_FILE) as file:
            csv_reader = csv.DictReader(file)
            w = 0

            for row in csv_reader:
                for team in teams:
                    if row["abb"] == team:
                        w += int(row['wins'])

        return "{}".format(w)

    def get_manager_record(self):
        teams = self.get_teams()

        with open(CSV_FILE) as file:
            csv_reader = csv.DictReader(file)
            w = 0
            l = 0
            t = 0

            for row in csv_reader:
                for team in teams:
                    if row['abb'] == team:
                        w += int(row['wins'])
                        l += int(row['losses'])
                        t += int(row['ties'])

        return "{}-{}-{}".format(w, l, t)

    def get_standings_points(self):
        record = self.get_manager_record()
        x = record.split("-")
        wins = float(x[0])
        ties = float(x[2])
        points = wins + (ties * .5)
        return points

    def get_pointsfor(self):
        teams = self.get_teams()

        with open(CSV_FILE) as file:
            csv_reader = csv.DictReader(file)
            x = 0

            for row in csv_reader:
                for team in teams:
                    if row["abb"] == team:
                        pf = row['points_for']
                        if pf == "":
                            x += 0
                        else:
                            x += int(pf)
        return "{}".format(x)

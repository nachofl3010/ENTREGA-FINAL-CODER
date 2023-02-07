from django.db import models
from tournaments.models import Tournaments

class Players(models.Model):
    name= models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Matches(models.Model):
    CHOICES=(
        ('Player 1', 'Player 1'),
        ('Player 2', 'Player 2'),
    )
    player_1=models.CharField(max_length=100)
    player_2=models.CharField(max_length=100)
    year=models.IntegerField()
    winner=models.CharField(choices=CHOICES, max_length=8)

class Results(models.Model):
    RESULT_CHOICES=(('WINNER','WINNER'),
    ('RUNNER-UP','RUNNER-UP'),
    ('SEMI-FINALIST','SEMI-FINALIST'),
    ('QUARTER-FINALIST','QUARTER-FINALIST'),
    ('ROUND OF 16','ROUND OF 16'),
    ('ROUND OF 32','ROUND OF 32'),('ROUND OF 64','ROUND OF 64'),
    ('ROUND OF 128','ROUND OF 128'))
    name=models.ForeignKey(Players, on_delete=models.CASCADE)
    #tournament=models.CharField(max_length=100)
    tournament=models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    result=models.CharField(choices=RESULT_CHOICES, max_length=100)
    points_earned=models.IntegerField()

    # def __str__(self):
    #     return self.name
    # class Meta:
    #     ordering=['name']
# class Results(models.Model):
#     name=models.CharField(max_length=100)
#     tournament=models.CharField(max_length=100)
#     result=models.CharField(max_length=100)
#     points_earned=models.IntegerField()



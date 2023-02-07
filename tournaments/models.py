from django.db import models

class Tournaments(models.Model):

    CHOICES=(
        ('GS', 'GS'),
        ('M1000', 'M1000'),
        ('ATP500','ATP500'),
        ('ATP250','ATP250')
    )
    name=models.CharField(max_length=100)
    category=models.CharField(choices=CHOICES, max_length=50)
    def __str__(self):
        return self.name



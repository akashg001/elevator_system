from django.db import models

class Elevator(models.Model):
    name = models.CharField(max_length=100)
    current_floor = models.IntegerField(default=0)
    is_moving = models.BooleanField(default=False)
    direction = models.CharField(max_length=10, choices=(('up', 'Up'), ('down', 'Down'), ('stop', 'Stop')))
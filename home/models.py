from django.db import models

class Elevator(models.Model):
    name = models.CharField(max_length=100)
    current_floor = models.IntegerField(default=0)
    is_running = models.BooleanField(default=False)
    is_door_open = models.BooleanField(default=False)
    direction = models.CharField(max_length=10, choices=(('up', 'Up'), ('down', 'Down'), ('stop', 'Stop')))
    requests = models.ManyToManyField('Request')

    def move_up(self):
        self.current_floor += 1

    def move_down(self):
        self.current_floor -= 1

    def open_door(self):
        self.is_door_open = True

    def close_door(self):
        self.is_door_open = False

    def start_running(self):
        self.is_running = True

    def stop_running(self):
        self.is_running = False

    def display_status(self):
        print(f"Elevator {self.name} | Current Floor: {self.current_floor} | Running: {self.is_running} | Door Open: {self.is_door_open}")


class Request(models.Model):
    floor = models.IntegerField()
    direction = models.CharField(max_length=10, choices=(('up', 'Up'), ('down', 'Down')))
    elevator = models.ForeignKey('Elevator', on_delete=models.CASCADE, related_name='requests')

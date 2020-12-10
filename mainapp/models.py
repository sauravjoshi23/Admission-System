from django.db import models

class Engineering(models.Model):

    name = models.CharField(max_length=200, blank=False)
    percentage = models.IntegerField()

    choices = (
        ('Applied', 'Admission applied'),
        ('Admit', 'Admitted')
    )

    status = models.CharField(max_length=10, choices=choices, default='Applied')
    number = models.CharField(max_length=50, default="-")

    class Meta:
        abstract = True
        ordering = ['-percentage']

    def __str__(self):
        return 'Name: {0} Percentage: {1}'.format(self.name, self.percentage)

class Computer(Engineering):
    pass

class IT(Engineering):
    pass

class Mechanical(Engineering):
    pass

class Electronics(Engineering):
    pass

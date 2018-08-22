from django.db import models


class DummyData(models.Model):
    date = models.DateField()
    first_value = models.IntegerField()
    second_value = models.IntegerField()

    def __str__(self):
        return str(self.date)

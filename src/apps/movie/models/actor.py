from django.db import models
from src.apps.common.models.base import CountryBase
from datetime import date


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    country = models.ForeignKey(CountryBase, on_delete=models.SET_NULL, null=True, related_name='actors')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def get_age(self):
    #     today = date.today()
    #     age = today.year - self.date_of_birth.year - (
    #                 (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    #     return age

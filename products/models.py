from django.db import models
from django.core.validators import MinValueValidator


class Question(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(0)])
    category = models.CharField(max_length=64, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.owner}"



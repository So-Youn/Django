from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=150)
    past_job = models.TextField()

    def __str__(self):
        return f'{self.name} : {self.past_job}'
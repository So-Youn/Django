from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    audience = models.IntegerField()
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=150)
    watch_grade = models.CharField(max_length=150)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id}번째 영화- {self.title} : {self.audience} : {self.open_date} : {self.genre}  : {self.watch_grade} : {self.score}'
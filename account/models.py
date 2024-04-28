from django.db import models

class Survey(models.Model):
    question = models.CharField(max_length=255)

class Answer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    choice = models.CharField(max_length=1, choices=(('A', 'A'), ('B', 'B')))
    description = models.CharField(max_length=255)
    movie_genre = models.CharField(max_length=100)  # Burada uygun film türlerini belirleyin
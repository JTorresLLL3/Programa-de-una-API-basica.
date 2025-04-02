import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # Usar timezone.now() para comparar con la fecha de publicación
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    correo = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
        return self.edad
        return self.correo
    

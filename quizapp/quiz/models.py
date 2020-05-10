from django.db import
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=500)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)


class QuizMap(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice)


class UserQuizMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)



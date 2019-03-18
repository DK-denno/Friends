from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="question")
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Answers(models.Model):
    Question = models.OneToOneField(Questions,on_delete=models.CASCADE,related_name="answer")
    answer = models.CharField(max_length=10)

    def __str__(self):
        return self.Question.question

class Choices(models.Model):
    Question = models.OneToOneField(Questions,on_delete=models.CASCADE,related_name="choice")
    choiceA = models.CharField(max_length=100)
    choiceB = models.CharField(max_length=100)
    choiceC = models.CharField(max_length=100)

    def __str__(self):
        return self.Question.question

class AnsweredQuestion(models.Model):
    User = models.ForeignKey(User,related_name='answerer')
    Question = models.ForeignKey(Questions,related_name="questionanswered")
    Answer = models.CharField(max_length=10)

    def __str__(self):
        return self.Answer


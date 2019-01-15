from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    question = models.name = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

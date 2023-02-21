from django.db import models


# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)
    word_class = models.CharField(max_length=1)
    personality = models.CharField(max_length=1)
    sample = models.CharField(max_length=50)
    polish_sample = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    last_question = models.DateTimeField('date published')
    num_answer = models.IntegerField(default=0)
    num_correct = models.IntegerField(default=0)
    ratio_correct = models.FloatField(default=0)
    user = models.IntegerField(default=0)


class Form(models.Model):
    name = models.ForeignKey(Word, on_delete=models.CASCADE)
    ich = models.CharField(max_length=50)
    du = models.CharField(max_length=50)
    er = models.CharField(max_length=50)
    wir = models.CharField(max_length=50)
    ihr = models.CharField(max_length=50)
    sie = models.CharField(max_length=50)


class Past(models.Model):
    name = models.ForeignKey(Word, on_delete=models.CASCADE)
    past_tense = models.CharField(max_length=50)


class Person(models.Model):
    name = models.ForeignKey(Word, on_delete=models.CASCADE)
    personality = models.CharField(max_length=1)


class Prular(models.Model):
    name = models.ForeignKey(Word, on_delete=models.CASCADE)
    personality = models.CharField(max_length=50)

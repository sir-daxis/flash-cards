from django.db import models


# Create your models here.
class AppUser(models.Model):
    user_name = models.CharField(max_length=15)

    def __str__(self):
        return ''.join([self.user_name, f' [{self.pk}]'])


class WordClass(models.Model):
    word_type = models.CharField(max_length=15)

    def __str__(self):
        return ''.join([self.word_type, f' [{self.pk}]'])


class Person(models.Model):
    personality = models.CharField(max_length=3)

    def __str__(self):
        return ''.join([self.personality, f' [{self.pk}]'])


class Word(models.Model):
    name = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)
    word_class = models.ForeignKey(WordClass, on_delete=models.CASCADE)
    personality = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    sample = models.CharField(max_length=150)
    polish_sample = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    last_question = models.DateTimeField()
    num_answer = models.IntegerField(default=0)
    num_correct = models.IntegerField(default=0)
    ratio_correct = models.FloatField(default=0)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)


    def __str__(self):
        return ''.join([self.name, f' [{self.pk}]'])


class Form(models.Model):
    name = models.ForeignKey(Word, on_delete=models.CASCADE)
    ich = models.CharField(max_length=50)
    du = models.CharField(max_length=50)
    er_es_sie = models.CharField(max_length=50)
    wir = models.CharField(max_length=50)
    ihr = models.CharField(max_length=50)
    sie_sie = models.CharField(max_length=50)

    def __str__(self):
        return ''.join([self.sie_sie, f' [{self.pk}]'])


class Past(models.Model):
    name = models.ForeignKey(Word, on_delete=models.CASCADE)
    past_tense = models.CharField(max_length=50)


class Plural(models.Model):
    name = models.ForeignKey(Word, on_delete=models.CASCADE)
    personality = models.CharField(max_length=50)

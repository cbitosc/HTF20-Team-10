from django.db import models
import datetime


from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
class cricket(models.Model):
    pname = models.CharField(max_length=200)
    psec = models.CharField(max_length=50)
    def __str__(self):
        return self.pname
class basketball(models.Model):
    pname = models.CharField(max_length=200)
    psec = models.CharField(max_length=50)
    def __str__(self):
        return self.pname
class kabaddi(models.Model):
    pname = models.CharField(max_length=200)
    psec = models.CharField(max_length=50)
    def __str__(self):
        return self.pname
class volleyball(models.Model):
    pname = models.CharField(max_length=200)
    psec = models.CharField(max_length=50)
    def __str__(self):
        return self.pname
class schedule(models.Model):
    team_a = models.CharField(max_length=50)
    team_b = models.CharField(max_length=50)
    dt=models.DateTimeField()
    game=models.CharField(max_length=50)
    def __str__(self):
        return self.game
class cricplayers(models.Model):
    playername=models.CharField(max_length=50)
    playerscore=models.IntegerField()
    playerdate=models.DateField()



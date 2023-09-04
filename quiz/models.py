from django.db import models
from django.utils import timezone


class questions(models.Model):

    ID = models.AutoField(primary_key=True)
    category = models.CharField("category", max_length=50)
    question = models.CharField("question", max_length=200)
    good_answer = models.CharField("good_answer", max_length=200)
    max_points_to_get = models.IntegerField("max_points_to_get", default=1)
    is_active = models.BooleanField()

    def __str__(self):

        return self.question


class changelog(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.TextField("title", max_length=20, default="test")
    info = models.TextField("info", max_length=500)
    timestamp = models.DateField(default=timezone.now)
    isNew = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title} , {self.timestamp}'


class DiscordBotRequests(models.Model):
    ID = models.AutoField(primary_key=True)
    info = models.TextField("info", max_length=100, default="test discord info")
    
    
    def __str__(self):
        return f'{self.ID} , {self.info}'

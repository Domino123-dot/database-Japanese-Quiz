from django.db import models

class questions(models.Model):

    ID = models.AutoField(primary_key=True)
    category = models.CharField("category" , max_length=50)
    question = models.CharField("question" ,max_length=200)
    good_answer = models.CharField("good_answer" , max_length=200)
    is_active = models.BooleanField()

    def __str__(self):

        return self.question

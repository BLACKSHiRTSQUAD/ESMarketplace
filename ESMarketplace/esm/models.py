from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExpertSystem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=80)
    create_date = models.DateTimeField('date created')
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title


class ESQuestion(models.Model):
    es = models.ForeignKey(ExpertSystem, on_delete=models.CASCADE)
    es_start_question = models.BooleanField(default=False)
    question_text = models.CharField(max_length=400)

    def __str__(self):
        return self.question_text


class ESChoice(models.Model):
    es_question = models.ForeignKey(ESQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=160)

    def __str__(self):
        return self.choice_text


class ESPurchased(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    es_id = models.ForeignKey(ExpertSystem, on_delete=models.PROTECT)


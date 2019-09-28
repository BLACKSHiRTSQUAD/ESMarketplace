from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class ExpertSystem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=80)
    create_date = models.DateTimeField('date created', default=timezone.now)
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title


class ESQuestion(models.Model):
    es_id = models.OneToOneField(ExpertSystem, on_delete=models.PROTECT, null=True, blank=True)
    next_questions_id = models.ForeignKey('self', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=160)
    question_text = models.CharField(max_length=400)
    leaf = models.BooleanField(default=False)
    leaf_text = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.question_text


class ESPurchased(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    es_id = models.ForeignKey(ExpertSystem, on_delete=models.PROTECT)


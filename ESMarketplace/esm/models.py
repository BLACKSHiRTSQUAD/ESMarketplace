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


# Creates a tree-like structure with nodes linked to each other
class ESQuestion(models.Model):
    # Only used for the first question in an ES
    es_id = models.OneToOneField(ExpertSystem, on_delete=models.PROTECT, null=True, blank=True)
    # Question that links to this question, and the choice_text that got us here
    prev_question_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    prev_choice_text = models.CharField(max_length=160, null=True, blank=True)
    # Following the previous choice, the new question text ...
    # OR ... if leaf node, the question_text is actually the answer text.
    qa_text = models.CharField(max_length=400)
    leaf = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.qa_text


class ESPurchased(models.Model):
    # customer user
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    # link to seller through es_id
    es_id = models.ForeignKey(ExpertSystem, on_delete=models.PROTECT)

    def __str__(self):
        return self.user_id


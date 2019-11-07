from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Company(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=True, null=True)
    company_admin = models.BooleanField(default=False, blank=True)
    site_admin = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ESCategoryOne(models.Model):
    category_title = models.TextField(max_length="40")

    def __str__(self):
        return self.category_title


# make escategory one a company actually. a company can add to an existing category then, but it won't show unless it's
# a part of the current company or global. when searching, the global categories and any customer defined categories can
# all be created then
class ESCategoryTwo(models.Model):
    category_one_id = models.ForeignKey(ESCategoryOne, on_delete=models.PROTECT, blank=True, null=True)
    category_title = models.TextField(max_length="40")

    def __str__(self):
        s = "{} - {}".format(self.category_one_id.__str__(), self.category_title)
        return s


class ESCategoryThree(models.Model):
    category_two_id = models.ForeignKey(ESCategoryTwo, on_delete=models.PROTECT, blank=True, null=True)
    category_title = models.TextField(max_length="40")

    def __str__(self):
        s = "{} - {}".format(self.category_two_id.__str__(), self.category_title)
        return s


class ExpertSystem(models.Model):
    owner = models.ForeignKey(Company, on_delete=models.PROTECT)
    title = models.CharField(max_length=80)
    create_date = models.DateTimeField('date created', default=timezone.now)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    category_id = models.ForeignKey(ESCategoryThree, on_delete=models.PROTECT)

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
    leaf = models.BooleanField(default=False, blank=True)

    def __str__(self):
        s = "CHOICE:{}---QUESTION:{}".format(self.prev_choice_text, self.qa_text)
        return s





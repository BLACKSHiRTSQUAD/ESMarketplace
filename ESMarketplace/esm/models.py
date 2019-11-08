from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Company with pk=1 is called GLOBAL, which is available to everyone.
class Company(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name

# The company of a profile is where all the ES's fall under, but a user does not need to belong to a company.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
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


# category_one_id is actually a Company, which is correctly the top level category.
class ESCategoryTwo(models.Model):
    category_one_id = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    category_title = models.TextField(max_length="40")

    def __str__(self):
        s = "{} - {}".format(self.category_one_id.__str__(), self.category_title)
        return s


class ESCategoryThree(models.Model):
    category_two_id = models.ForeignKey(ESCategoryTwo, on_delete=models.CASCADE, blank=True, null=True)
    category_title = models.TextField(max_length="40")

    def __str__(self):
        s = "{} - {}".format(self.category_two_id.__str__(), self.category_title)
        return s


class ExpertSystem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    title = models.CharField(max_length=80)
    create_date = models.DateTimeField('date created', default=timezone.now)
    category_id = models.ForeignKey(ESCategoryThree, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


# Creates a tree-like structure with nodes linked to each other
class ESQuestion(models.Model):
    # Only used for the first question in an ES
    es_id = models.OneToOneField(ExpertSystem, on_delete=models.CASCADE, null=True, blank=True)
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





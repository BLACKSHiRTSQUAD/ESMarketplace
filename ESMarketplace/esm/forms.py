from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import *


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class AccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disabled_fields = ['username', 'email', 'first_name', 'last_name']
        for disabled_field in disabled_fields:
            self.fields[disabled_field].widget.attrs['disabled'] = 'true'
            self.fields[disabled_field].widget.attrs['class'] = 'myCustomClass'


class CreateESForm(ModelForm):
    class Meta:
        model = ExpertSystem
        fields = ['title', 'cost']


class QuestionChoicesForm(ModelForm):
    class Meta:
        model = ESQuestion
        fields = ['prev_choice_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disabled_fields = ['prev_choice_text']
        for disabled_field in disabled_fields:
            self.fields[disabled_field].widget.attrs['disabled'] = 'true'
            self.fields[disabled_field].widget.attrs['class'] = 'myCustomClass'







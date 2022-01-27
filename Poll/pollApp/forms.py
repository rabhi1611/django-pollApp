from dataclasses import field, fields
from django.forms import ModelForm
from pollApp import models

class create_poll_form(ModelForm):
    class Meta:
        model = models.Poll
        fields = {'question', 'option_1', 'option_2', 'option_3'}
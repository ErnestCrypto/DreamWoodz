from django import forms
from django.forms import ModelForm
from .models import *
from rest_framework import serializers


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"


















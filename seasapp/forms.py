from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from seasapp.models import *
from django.core.exceptions import ValidationError
import os


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

# upload file


class uploadfileform(forms.ModelForm):

    class Meta:
        model = uploadedfiles
        fields = ('File_to_upload',)

    def clean(self):
        file_path = "media//Resources//" + str(self.cleaned_data.get('File_to_upload'))
        file_path = file_path.replace(" ", "_")
        file_path = file_path.replace("(", "")
        file_path = file_path.replace(")", "")
        if os.path.isfile(file_path):
            raise ValidationError('File already exists')
        return self.cleaned_data

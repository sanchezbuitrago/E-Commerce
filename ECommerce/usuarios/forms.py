# coding: utf-8
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
 
from .models import CustomUser, LinkedInUser
 
class CustomUserCreationForm(UserCreationForm):
 
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

class LinkedInUserCreationForm(UserCreationForm):
    linkedin_id = forms.CharField(label="LinkedIn Id", max_length=30, required=False,
                                  help_text="Required. 30 characters or fewer.")
 
    class Meta:
        model = LinkedInUser
        fields = ('username','linkedin_id','first_name','last_name')
 
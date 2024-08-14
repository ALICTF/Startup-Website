from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class SignupForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'job', 'gender')
        

class ChangeUserForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = "__all__"
        
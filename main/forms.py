from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        
class ReviewForm(ModelForm):
    class Meta:
        model = ReviewMessage
        fields = '__all__'

class ForgotForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']
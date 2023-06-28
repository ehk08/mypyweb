from django.contrib.auth.forms import UserCreationForm
from django.forms import forms


class UserForm(UserCreationForm):
    last_name = forms.Charfield()
    email = forms.EmailField()

class Meta:
    model = User
    fields = ['username', 'last_name', 'email']

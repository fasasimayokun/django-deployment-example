from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import MyFruit


from django.forms.widgets import PasswordInput, TextInput

# register/ create a user

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
'''
    class Meta:
        model = User
        fields = ['username', 'password']
'''

# create a new fruits

class AddFruit(forms.ModelForm):

    class Meta:
        model = MyFruit
        fields = ['image', 'name', 'category', 'description']

    def __init__(self, *args, **kwargs):
        super(AddFruit, self).__init__(*args, **kwargs)

        
        #self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['name'].label = ''

        self.fields['category'].widget.attrs['placeholder'] = 'category'
        self.fields['category'].label = ''

        self.fields['description'].widget.attrs['placeholder'] = 'description'
        self.fields['description'].label = ''

class UpdateFruit(forms.ModelForm):

    class Meta:
        model = MyFruit
        fields = ['image', 'name', 'category', 'description'] 
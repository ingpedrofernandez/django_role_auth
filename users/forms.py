from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Client



class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False, help_text='A valid email address, please.')
    password1 = forms.CharField(label='Enter password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password1']
        help_texts = {
            'username': None,
        }



class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email']
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False


class ProfilePictureForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False, label='Change Profile Photo')
    #role = forms.CharField(widget=forms.HiddenInput(), initial="user")

    class Meta:
        model = Profile
        fields = ['profile_pic']


class ClientAddForm(forms.ModelForm):
    user = forms.CharField(max_length=100, required=False)
    firstname = forms.CharField(max_length=100, required=False)
    lastname = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    mobile = forms.IntegerField()
    client_pic = forms.ImageField(required=False, label='Change Client Photo')

    class Meta:
        model = Client
        fields = ['user', 'firstname', 'lastname', 'email', 'mobile', 'client_pic']
        help_texts = {
            'email': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False




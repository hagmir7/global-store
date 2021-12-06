from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.forms.widgets import Widget
from django.utils.translation import gettext as _
from .models import Profile


# LogIn Form
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

    # Clean Username
    def clean_username(self):
        clean_data = self.cleaned_data
        if not User.objects.filter(username=clean_data['username']).exists():
            raise ValidationError(_('There is no registered user with this name!'))
        return clean_data['username']

# SigIn Form
class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.PasswordInput()


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


    # Clean Username
    def clean_username(self):
        clean_data = self.cleaned_data
        if User.objects.filter(username=clean_data['username']).exists():
            raise ValidationError(_('There is a registered user with this username!'))
        return clean_data['username']
    
    # Clean Password
    # def clean_password(self):
    #     clean_data = self.cleaned_data
    #     if clean_data['password'] == clean_data['password']:
    #         raise ValidationError(_('Password dose ot match.'))
    #     return clean_data['password2']

    # Clean Email
    def clean_email(self):
        clean_data = self.cleaned_data
        if User.objects.filter(email=clean_data['email']).exists():
            raise ValidationError(_('There is a registered user with this email!'))
        return clean_data['email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'cover', 'phone', 'gander', 'country', 'bio')



class UserUpdateInfo(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def clean(self):
        cleaned_data = super(PasswordChange, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_('The two passwords did not match'))
        return cleaned_data
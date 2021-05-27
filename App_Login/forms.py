from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from .models import UserProfile


class CreateNewUser(UserCreationForm):
   email = forms.EmailField(required=True,label = "", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
   username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
   password1 = forms.CharField(required=True,label="",widget = forms.PasswordInput(attrs={'placeholder':'Password'}))
   password2 = forms.CharField(required=True,label="",widget = forms.PasswordInput(attrs={'placeholder':'Password Confirmation'}))
   class Meta:
    model = User
    fields = ('email','username','password1','password2')


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileChange(UserChangeForm):
    class Meta:
        model =User
        fields = ('email','username','first_name','last_name','password')


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)


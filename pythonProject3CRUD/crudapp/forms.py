from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from crudapp.models import Login, Student,Book


class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)

    class Meta:
        model=Login
        fields=('username','password1','password2')
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=('user',)
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'



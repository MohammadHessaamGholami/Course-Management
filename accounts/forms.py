from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import TextInput

from accounts.models import Student, Teacher


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False,
                                 widget=TextInput(attrs={'class': 'form-control', 'maxlength': 100}), )
    last_name = forms.CharField(max_length=100, required=False,
                                widget=TextInput(attrs={'class': 'form-control', 'maxlength': 100}))

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_id',)
        widgets = {'student_id': TextInput(attrs={'class': 'form-control', 'maxlength': 10})}


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('teacher_id', 'started_at')
        widgets = {
            'teacher_id': TextInput(attrs={'class': 'form-control', 'maxlength': 10}),
            'started_at': TextInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class LoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label='رمز عبور',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )

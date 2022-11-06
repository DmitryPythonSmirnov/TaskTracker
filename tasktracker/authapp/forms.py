from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import TaskUser


class TaskUserLoginForm(AuthenticationForm):
    class Meta:
        model = TaskUser
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super(TaskUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TaskUserRegisterForm(UserCreationForm):
    class Meta:
        model = TaskUser
        fields = ('username', 'password1', 'password2', 'email', 'age')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class TaskUserEditForm(UserChangeForm):
    class Meta:
        model = TaskUser
        fields = ('username', 'email', 'age', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_test = ''

            # Спрятали поле с паролем
            if field_name == 'password':
                field.widget = forms.HiddenInput()

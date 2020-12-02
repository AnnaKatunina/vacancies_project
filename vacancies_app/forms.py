from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from vacancies_app.models import Application


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'h6 font-weight-light'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
            ),
            ButtonHolder(
                Submit('submit', 'Зарегистрироваться', css_class='btn btn-primary btn-lg btn-block')
            )
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин")

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'text-muted'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'password',
            ),
            ButtonHolder(
                Submit('submit', 'Войти', css_class='btn btn-primary btn-lg btn-block')
            )
        )


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'written_username',
                'written_phone',
                'written_cover_letter',
            ),
            ButtonHolder(
                Submit('submit', 'Отправить отклик', css_class='btn btn-primary mt-4 mb-2')
            )
        )

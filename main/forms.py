from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import CustomUser
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext as _

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Give a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and CustomUser.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                CustomUser._meta.get_field('username').error_messages['unique'],
                code='unique'
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                CustomUser._meta.get_field('email').error_messages['unique'],
                code='unique'
            )
        return email

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label="",
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': _('Username')}),
    )
    password = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': _('Password')}),
    )

from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError

User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Имя'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Почта'}))
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class PasswordChangeForm(forms.Form):
#     current_password = forms.CharField(label='current_password', widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Текущий пароль'}))
#     password_new = forms.CharField(label='password_new', widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль'}))
#     password_new2 = forms.CharField(label='password_new2', widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))
#
#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super().__init__(*args, **kwargs)
#
#     def clean_new_password2(self):
#         password1 = self.cleaned_data.get("new_password1")
#         password2 = self.cleaned_data.get("new_password2")
#         if password1 and password2:
#             if password1 != password2:
#                 raise ValidationError(
#                     self.error_messages["password_mismatch"],
#                     code="password_mismatch",
#                 )
#         password_validation.validate_password(password2, self.user)
#         return password2
#
#     def save(self, commit=True):
#         password = self.cleaned_data["new_password1"]
#         self.user.set_password(password)
#         if commit:
#             self.user.save()
#         return self.user

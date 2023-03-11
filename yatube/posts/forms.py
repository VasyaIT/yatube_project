from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Почта'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Тема'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Отзыв'}))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')
    #
    # def clean_subject(self):
    #     data = self.cleaned_data['subject']
    #
    #     # Если пользователь не поблагодарил администратора - считаем это ошибкой
    #     if 'спасибо' not in data.lower():
    #         raise forms.ValidationError('Вы обязательно должны нас поблагодарить!')
    #
    #     # Метод-валидатор обязательно должен вернуть очищенные данные,
    #     # даже если не изменил их
    #     return data

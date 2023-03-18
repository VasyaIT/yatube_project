from .models import Contact, Comment
from django import forms


class ContactForm(forms.ModelForm):
    email = forms.EmailField(label='Почта')
    subject = forms.CharField(label='Тема')
    body = forms.CharField(label='Отзыв')

    class Meta:
        model = Contact
        fields = ('email', 'subject', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

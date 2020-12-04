from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    sender = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(label='Телефон', widget=forms.NumberInput(attrs={"class":"form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows":"6"}), label='Текст сообщения', max_length=500)
    captcha = CaptchaField()
from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
	name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={"name":"name", "placeholder":"Имя*"}))
	sender = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"name":"email", "placeholder":"E-mail*"}))
	phone = forms.CharField(label='Телефон', widget=forms.NumberInput(attrs={"name":"phone", "placeholder":"Телефон"}))
	message = forms.CharField(widget=forms.Textarea(attrs={"name":"message", "placeholder":"Сообщение*", "rows":"4"}), max_length=500)
	captcha = CaptchaField()
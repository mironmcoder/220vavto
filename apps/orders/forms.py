from django import forms
from .models import Order
from captcha.fields import CaptchaField


class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['name', 'phone', 'email', 'address', 'comment']
		widgets = {
			'name': forms.TextInput(attrs={"placeholder":"Имя*"}),
			'phone': forms.TextInput(attrs={"placeholder":"Телефон*"}),
			'email': forms.TextInput(attrs={"placeholder":"Email*"}),
			'address': forms.TextInput(attrs={"placeholder":"Адрес*"}),
			'comment': forms.Textarea(attrs={"placeholder":"Комментарий*"}),
			}
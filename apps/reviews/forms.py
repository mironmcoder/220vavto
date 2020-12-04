from django import forms
from .models import Reviews
from captcha.fields import CaptchaField

class ReviewsForm(forms.ModelForm):
	captcha = CaptchaField()

	class Meta:
		model = Reviews
		fields = ("username", "email", "comment", "captcha")

		widgets = {
			"username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя", "type":"text", "id":"inputName"}),
			"email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email", "type":"email", "id":"inputEmail4"}),
			"comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Комментарий", "id":"exampleFormControlTextarea1", "rows":"5"})
        }

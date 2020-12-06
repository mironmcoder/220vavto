from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView 
from apps.product.models import *
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

class IndexListView(ListView):
	queryset = ProductCart.objects.filter(is_active=1).order_by('-pub_date')
	template_name = 'index.html'

def contact(request):
	form = ContactForm()
	return render(request, 'contact.html', {'form':form})

def contact_send(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			message = '''
					<h1 style="text-align:center"> Имя: %(name)s </h1> <br> 
					<h1 style="text-align:center"> Email: %(sender)s </h1> <br>
					<h1 style="text-align:center"> Телефон: %(phone)s </h1> <br>
					<h1 style="text-align:center"> Текст: %(message)s </h1> <br>''' % form.cleaned_data
			send = send_mail(
				subject = 'Форма обратной связи',
				message = '',
				recipient_list = ['220vavto@mail.ru'],
				from_email = '220vavto@mail.ru',
				fail_silently = True,
				html_message = message
			)
			if send:
				return HttpResponse(status=201)
		else:
			return HttpResponse(status=404)

def help(request):
	return render(request, 'help.html')

def delivery(request):
	return render(request, 'delivery.html')


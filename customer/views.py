from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django import forms

from customer.forms import RegisterForm

# to do: customer/account



# Create your views here.

def login(request):
	return render(request, 'login.html');

def create(request):
	if (request.method == 'POST'):
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/custoemr/create')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form,})

def loginPost(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/customer/account/')
	else:
		return HttpResponseRedirect('/customer/account/invalid')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
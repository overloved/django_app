# from django.core.mail import send_email
from django.http import HttpResponse
from django.shortcuts import render
from contact.forms import ContactForm

def contact(request):
	errors = []
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			# send_email(
			# 	data['subject'],
			# 	data['message'],
			# 	data.get('email', 'noreply@example.com'),
			# 	['siteowner@example.com'],
			# 	)
			return HttpResponseRedirect('/contact-us/thanks')
	else:
		form = ContactForm()
			# initial={'subject': 'I love your site!'}
			
	return render(request, 'contact_form.html', { 'form': form })
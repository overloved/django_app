from django import forms
from django.contrib import auth
from customer.models import UserEntity

import re

alnum_re = re.compile(r'^\w+$')

class RegisterForm(forms.ModelForm):
	fname = forms.CharField(
		label = "First Name",
		max_length = 30,
		widget = forms.TextInput(),
		required= True
	)
	lname = forms.CharField(
		label = "Last Name",
		max_length = 30,
		widget = forms.TextInput(),
		required= True
	)
	# username = forms.CharField(
 #        label = "Username",
 #        max_length = 30,
 #        widget = forms.TextInput(),
 #        required = True
 #    )
	# # password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	# email = forms.EmailField(
 #        label = "Email",
 #        widget = forms.TextInput(), 
 #        required = True
 #    )
	# password = forms.CharField(
	# 	label = "Password", 
	# 	widget = forms.PasswordInput(render_value=False)
	# )
	password_confirm = forms.CharField(
		label = "Password (again)", 
		widget = forms.PasswordInput(render_value=False)
	)
	
	class Meta:
		model = UserEntity
		fields = ['fname', 'lname', 'username', 'email', 'password']    

    # code = forms.CharField(
    #     max_length=64,
    #     required=False,
    #     widget=forms.HiddenInput()
    # )

	def clean_username(self):
		username = self.cleaned_data['username']
		if not alnum_re.search(username):
			raise forms.ValidationError(_('Username can only contain letters, numbers and underscores.'))
		qs = UserEntity.objects.filter(username=username)
		if not qs.exists():
			return username
		raise forms.ValidationError('This username is already taken. Please choose another.')

	def clean_email(self):
		email = self.cleaned_data['email']
		qs = UserEntity.objects.filter(email=email)
		if not qs.exists():
			return email
		raise forms.ValidationError('This email address has already been registered.')

	def clean(self):
		if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
				raise forms.ValidationError('You must type the same password.')
		return self.cleaned_data






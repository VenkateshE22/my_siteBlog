from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Account
		fields = ("username", "email", "phonenumber", "is_author", "is_staff", "password1", "password2",)
		#fields= '__all__'
		#exclude=['is_staff','is_active','is_superuser']

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from blog.models import Author
from django.contrib.auth.models import User

# Create your views here.


def register_request(request):
	if request.method == "POST":
		usertype=request.POST['usertype']
		print(usertype)
		form = NewUserForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			
			if usertype=='Author':
				author=Author(user_key=user)
				author.save()
			elif usertype=='Admin':
				user.is_staff=True
				user.is_superuser=True
				user.save()
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="account/register.html", context={"register_form":form}
	)    

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="account/login.html", context={"login_form":form})    

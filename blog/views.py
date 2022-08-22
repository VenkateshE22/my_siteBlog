from django.shortcuts import render, redirect
from datetime import date
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError

all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image":"https://images.unsplash.com/photo-1551632811-561732d1e306?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGlraW5nfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "author":"Venkatesh",
        "date": date(2022,8,22),
        "title":"Mountain Hiking",
        "excerpt":"There's nothing like the views you get once you reach the top of a mountain.",
        "content":"//lh3.googleusercontent.com/vs9PHXnO9jte8eKhOzC4yIfr9BP3xChTOAx8yglRdZrJmJSefVJTzkUmnSxzodfWhMaWuMa8zBhK"
    },
    {
        "slug": "programming-is-fun",
        "image": "https://user-images.githubusercontent.com/48228083/58296201-92e44080-7d87-11e9-8c9f-39acfd48b438.png",
        "author": "Venkatesh",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": "//lh3.googleusercontent.com/vs9PHXnO9jte8eKhOzC4yIfr9BP3xChTOAx8yglRdZrJmJSefVJTzkUmnSxzodfWhMaWuMa8zBhK"
    },

    {
        "slug": "into-the-woods",
        "image": "https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1060&t=st=1661162196~exp=1661162796~hmac=4c5b6a0e72319ee37c4b45a0bdf9fe60baa5b13ee1eafe622d4c790c151c118a",
        "author": "Venkatesh",
        "date": date(2022, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": "//lh3.googleusercontent.com/vs9PHXnO9jte8eKhOzC4yIfr9BP3xChTOAx8yglRdZrJmJSefVJTzkUmnSxzodfWhMaWuMa8zBhK"
    },
]

# Create your views here.

def index(request):
	return render(request,"blog/index.html")

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts":latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts":all_posts})

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html",{"post":identified_post})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="blog/register.html", context={"register_form":form})    

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
	return render(request=request, template_name="blog/login.html", context={"login_form":form})    
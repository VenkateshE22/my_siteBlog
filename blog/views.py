from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import UploadDataForm
from account.models import User
from django.contrib import messages



# Create your views here.

def index(request):
	return render(request,"blog/index.html")


def starting_page(request):
    latest_posts = Post.objects.all().order_by("date")[:3]
    return render(request, "blog/index.html", {"posts":latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts":all_posts})

def post_detail(request, slug):

    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html",{"post":identified_post})

def upload(request):
    context = {}
    if request.method=='POST':
        # slug=request.POST['slug']
        title=request.POST['title']
        content=request.POST['content']
        excerpt=request.POST['excerpt']
        #author_obj=Author.objects.get(user_key=request.user)
        user_obj=User.objects.get(username=request.user.username)
        if user_obj.is_author:
            post_obj=Post(title=title,excerpt=excerpt,content=content,author=user_obj)
            post_obj.save()
            if request.FILES:
                post_obj=Post.objects.get(title=title)
                image=request.FILES['image']
                post_obj.image=image
                post_obj.save()

            return redirect("/")
        messages.warning(request,"You are not an author, sorry you can not post.")
        return redirect("/")      
        
    form=UploadDataForm()
    context['form'] = form
    
    return render (request,"blog/upload.html", context)
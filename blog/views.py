from multiprocessing import context
from re import template
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import UploadDataForm, catagoryForm, UpdateDataForm
from account.models import User
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def starting_page(request):
    latest_posts = Post.objects.filter(status="P").order_by("date")[
        :3
    ]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.filter(status="P").order_by("-date")
    return render(
        request, "blog/all-posts.html", {"all_posts": all_posts}
    )


def dashboard(request):
    if request.user.is_authenticated and request.user.is_author:
        draft_post = Post.objects.filter(
            status="D", author=request.user
        ).order_by("-date")
        published_posts = Post.objects.filter(
            status="P", author=request.user
        ).order_by("-date")
        return render(
            request,
            "blog/draft_posts.html",
            {
                "draft_post": draft_post,
                "published_post": published_posts,
            },
        )
    messages.warning(request, "Sorry your are not authorized")
    return redirect("/")


def post_detail(request, slug):

    identified_post = get_object_or_404(Post, slug=slug)
    return render(
        request, "blog/post-detail.html", {"post": identified_post}
    )


def upload(request):
    if request.user.is_authenticated and request.user.is_author:

        context = {}
        if request.method == "POST":
            # slug=request.POST['slug']
            title = request.POST["title"]
            content = request.POST["content"]
            excerpt = request.POST["excerpt"]
            # author_obj=Author.objects.get(user_key=request.user)

            user_obj = User.objects.get(
                    username=request.user.username
                )
            if request.POST["status"] == "P":
                post_obj = Post(
                        title=title,
                        excerpt=excerpt,
                        content=content,
                        author=user_obj,
                    status="P",
                    )
                post_obj.save()
                if request.FILES:
                    post_obj = Post.objects.get(title=title)
                    image = request.FILES["image"]
                    post_obj.image = image
                    post_obj.save()
            else:
                post_obj = Post(
                        title=title,
                        excerpt=excerpt,
                        content=content,
                        author=user_obj,
                        status="D",
                    )
                post_obj.save()
                if request.FILES:
                    post_obj = Post.objects.get(title=title)
                    image = request.FILES["image"]
                    post_obj.image = image
                    post_obj.save()
            return redirect("/")

        form = UploadDataForm()
        context["form"] = form
        return render(request, "blog/upload.html", context)
    messages.warning(request, "Sorry your are not authorized")
    return redirect("/")


def category_view(request):

    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        if request.user.is_author:
            post_obj1 = Category(name=name, description=description)
            post_obj1.save()
            return redirect("/")
    return render(
        request, "blog/add_category.html", {"form": catagoryForm}
    )


def update_blog(request, slug):
    if request.user.is_authenticated and request.user.is_author:

        context = {}
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["content"]
            excerpt = request.POST["excerpt"]
            status = request.POST["status"]
            category = request.POST["category"]
            if request.user.is_author:
                post_obj = Post.objects.get(slug=slug)
                if title:
                    post_obj.title = title
                if content:
                    post_obj.content = content

                if excerpt:
                    post_obj.excerpt = excerpt
                if status:
                    post_obj.status = status
                if category:
                    cat_object = Category.objects.get(id=int(category))
                    post_obj.category = cat_object

                if request.FILES:

                    image = request.FILES["image"]
                    if image:
                        post_obj.image = image

                post_obj.save()
                # post_obj2 = Post(title=title, content=content, excerpt=excerpt)
                # post_obj2.save()
                return redirect("/")
        form1 = UpdateDataForm()
        post_obj = Post.objects.get(slug=slug)
        return render(
            request,
            "blog/update_blog.html",
            {"form": form1, "post_obj": post_obj},
        )
    messages.warning(request, "Sorry your are not authorized")
    return redirect("/")


def delete_blog(request, slug):
    if request.user.is_authenticated and request.user.is_author:

        post_obj = Post.objects.get(slug=slug)
        if request.user.username == post_obj.author.username:
            post_obj.delete()
            messages.success(request, "blog deleted")
            return redirect("my-posts")
        messages.warning(request, "you can not delete other peoples blog")
        return redirect("my-posts")
    messages.warning(request, "Sorry your are not authorized")
    return redirect("/")

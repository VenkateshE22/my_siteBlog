from django.contrib import admin
from .models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date")
    list_display = ("id","title", "date", "author")

admin.site.register(Post,PostAdmin)
@admin.register(Category)
class catAdmin(admin.ModelAdmin):
    list_display=['id','name']

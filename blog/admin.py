from django.contrib import admin
from .models import Post, Comment


# Register your models here.
from django.contrib import admin
from .models import Post

admin.site.register(Post)
admin.site.register(Comment)

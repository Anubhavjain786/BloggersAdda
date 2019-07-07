from django.contrib import admin

# Register your models here.
from Blog.models import Post

admin.site.register(Post)
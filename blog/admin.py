from django.contrib import admin

# Register your models here.
from .models import Post, Projects
admin.site.register(Post)
admin.site.register(Projects)


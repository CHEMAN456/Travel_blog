from django.contrib import admin
from .models import TravelBlogPost,Comment,Category

# Register your models here.

admin.site.register(TravelBlogPost)
admin.site.register(Comment)
admin.site.register(Category)


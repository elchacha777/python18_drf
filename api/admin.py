from django.contrib import admin
from api.models import Category, Product, Like, Comment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)
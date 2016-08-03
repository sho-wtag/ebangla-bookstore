from django.contrib import admin

# Register your models here.
from .models import User
from .models import Category
from .models import Book

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Book)

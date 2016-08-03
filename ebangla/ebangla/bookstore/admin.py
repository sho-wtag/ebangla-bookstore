from django.contrib import admin

# Register your models here.
from .models import User
from .models import Category
from .models import Book
from .models import User_Wishlist

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(User_Wishlist)
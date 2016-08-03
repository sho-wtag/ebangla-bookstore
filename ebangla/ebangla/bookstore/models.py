from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.email


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    book_category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

class User_Wishlist(models.Model):
    created_by = models.ForeignKey(User)
    books = models.ManyToManyField(Book, null=True)

    def __str__(self):
        return self.created_by
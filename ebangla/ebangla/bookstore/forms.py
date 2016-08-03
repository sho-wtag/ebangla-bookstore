from django.forms import ModelForm
from ebangla.bookstore.models import *
from ebangla.bookstore.models import Book
from ebangla.bookstore.models import User


class SignupForm(ModelForm):
    class Meta:
        model=User

class BookForm(ModelForm):
    class Meta:
        model=Book

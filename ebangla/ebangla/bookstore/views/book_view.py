from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from ebangla.bookstore.models import Book


def add_book(request):
    if request.method=='POST':
        book_obj=Book(name=request.POST.get('name'),user_id=request.session['user_id'])
        book_obj.save()
        return HttpResponseRedirect('/')
    else:
        data=RequestContext(request,{'first_name':request.session['first_name']})
        return render_to_response('add_book.html',data)

def edit_book(request,book_id):
    if request.method=='POST':
        name=Book.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('book'))
        return HttpResponseRedirect('/')
    else:
        name=Book.objects.filter(id=book_id)
        data=RequestContext(request,{'first_name':request.session['first_name'],'book':name[0]})
        return render_to_response('edit_book.html',data)

def delete_book(request,book_id):
    Book.objects.get(id=book_id).delete()
    return HttpResponseRedirect('/')

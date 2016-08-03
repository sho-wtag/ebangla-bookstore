from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from ebangla.bookstore.models import User
from ebangla.bookstore.forms import SignupForm


def main_page(request):
    if 'user_id' in request.session:
        user_obj=User.objects.filter(id=request.session['user_id'])
        user1_obj=User.objects.filter(user_id=request.session['user_id'])
        data=RequestContext(request,{'first_name':request.session['first_name'],'user':user_obj,'user':user1_obj,'a':0})
        return render_to_response('user.html',data)
    else:
        form = SignupForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('index.html', variables)

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            obj=form.save()
            id=obj.id
            request.session['user_id']=id
            request.session['first_name']=form.cleaned_data['first_name']
    return HttpResponseRedirect('/')

def login(request):
    user_obj=User.objects.filter(email=request.POST.get('email'),password=request.POST.get('password'))
    if user_obj.count():
        print user_obj
        request.session['user_id']=user_obj[0].id
        request.session['first_name']=user_obj[0].first_name
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['user_id']
    del request.session['first_name']
    request.session.modified=True
    return HttpResponseRedirect('/')
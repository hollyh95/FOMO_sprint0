from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

@view_function
def process_request(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')

    context = {
    }
    return request.dmp.render('login.html', context)

from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from account import models
from formlib import Formless

@view_function
def process_request(request):
    form = LoginForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/account/index/')

    context = {
        'form': form
    }
    return request.dmp.render('login.html', context)

class LoginForm(Formless):
    def init(self):
        self.fields['email'] = forms.EmailField(label='Email')
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput())
        self.user = None

    def clean(self):
        self.user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid email or password.')
        return self.cleaned_data

    def commit(self):
        login(self.request, self.user)

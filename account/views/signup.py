from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from account import models as amod
from formlib import Formless
import re


@view_function
def process_request(request):
    form = SignupForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/account/login/')

    context = {
        'form': form
    }
    return request.dmp.render('signup.html', context)

class SignupForm(Formless):
    def init(self):
        self.fields['firstName'] = forms.CharField(label='First Name', max_length=100)
        self.fields['lastName'] = forms.CharField(label='Last Name', max_length=100)
        self.fields['email'] = forms.EmailField(label='Email', max_length=100)
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        checkEmail = amod.User()
        checkEmail = amod.User.objects.filter(email=email).first()
        if checkEmail is not None:
            raise forms.ValidationError('Email already exists')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be more than 8 characters long')
        if hasNumbers(password) == False:
            raise forms.ValidationError('Password must contain a number')
        return password

    def clean(self):
        password = self.cleaned_data.get('password')
        confirmPassword = self.cleaned_data.get('password2')
        if password != confirmPassword:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data

    def commit(self):
        newUser = amod.User()
        newUser.first_name = self.cleaned_data.get('firstName')
        newUser.last_name = self.cleaned_data.get('lastName')
        newUser.email = self.cleaned_data.get('email')
        newUser.set_password(self.cleaned_data.get('password'))
        newUser.save()

def hasNumbers(str):
    return bool(re.search(r'\d', str))












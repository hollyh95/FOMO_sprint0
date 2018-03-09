from django_mako_plus import view_function
from django import forms
from django.http import HttpResonseRedirect
from formlib.form import Formless

@view_function
def process_request(request):
    # process the form
    if request.method == 'POST':
        form = TestForm(request, request.POST)
        if form.is_valid():

            # work of the form - create user, login user, purchase
            return HttpResonseRedirect('/')

    else:
        form = TestForm()

    # render the form
        context = {
            'form' : form,

        }
        return request.dmp.render('formtest.html', context)

class TestForm(Formless):

        def init(self):
            self.fields['username'] = forms.CharField(label='Username')
            self.fields['age'] = forms.IntegerField(label='Your age')
            self.fields['renewal_date'] = forms.DateField(help_text= "Enter a date between now and 4")

        def clean_age(self):
            age = self.cleaned_data.get('age')
            if age <18:
                #show an error message: no soup for you
                print('>>>>> LESS THAN 18')
            return age

        def clean(self):
            # for checking the entire form - usually two variables at once
            #  "password" and "password2"
            pw1 = self.cleaned_data.get('password')
            pw2 = self.cleaned_data.get('password2')
            #if pw1 != pw2:
                # yell at the user

            return self.cleaned_data














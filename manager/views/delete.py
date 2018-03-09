from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from catalog import models as cmod


@view_function
def process_request(request, Product:cmod.Product=None):

    Product.status = 'I'
    Product.save()

    return HttpResponseRedirect('/manager/index/')
    context = {
    }
    return request.dmp.render('index.html',
        context
    )

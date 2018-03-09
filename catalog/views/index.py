from django_mako_plus import view_function, jscontext
from catalog import models as cmod
import math

@view_function
def process_request(request, Category:cmod.Category=None):

   clist = cmod.Category.objects.all()
   if Category is not None:
       pList = cmod.Product.objects.filter(category=Category)
       catid = Category.id
   else:
       pList = cmod.Product.objects.all()
       catid = 0


   maxPages = math.ceil(len(pList)/6)

   context = {
       'clist': clist,
       'selected': Category,
       'maxPages': maxPages,
       jscontext('catid'): catid,
   }
   return request.dmp.render('index.html', context)

@view_function
def inner(request, Category:cmod.Category=None, pnum:int=1):
    products = cmod.Product.objects.all()
    categories = cmod.Category.objects.all()

    if Category is not None:
        qry = products.filter(category=Category)
    else:
        qry = products

    splice = qry[(pnum-1)*6:pnum*6]

    context = {
        'splice': splice
    }
    return request.dmp.render('index.inner.html', context)



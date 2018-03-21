from django_mako_plus import view_function, jscontext
from catalog import models as cmod

@view_function
def process_request(request, Product:cmod.Product=None):
    name = Product.name
    description = Product.description
    price = Product.price
    main = Product.images.all().first()
    productType= type(Product).__name__

    if productType == "BulkProduct":
        quantity = Product.quantity
    else:
        quantity=-1

    if main is None:
        mainImage = 'notfound.jpg'
    else:
        mainImage= main.filename

    lastFive = request.session.get('lastFive')
    lastFiveProds = []
    if len(lastFive) < 5:
        for product in lastFive:
            lastFiveProds.insert(0, cmod.Product.objects.get(id=product))
    else:
        for x in range (len(lastFive) - 5, len(lastFive)):
            lastFiveProds.insert(0, cmod.Product.objects.get(id=lastFive[x]))

    if Product.id not in lastFive:
        lastFive.append(Product.id)
    else:
        lastFive.remove(Product.id)
        lastFive.append(Product.id)

    request.session['lastFive'] = lastFive

    clist = cmod.Category.objects.all()

    context = {
        'imageList': Product.images.all(),
        'name': name,
        'description': description,
        'price': price,
        'mainImage': mainImage,
        'clist': clist,
        'productType': productType,
        'quantity': quantity,
        'lastFiveProds': lastFiveProds,
    }
    return request.dmp.render('details.html', context)

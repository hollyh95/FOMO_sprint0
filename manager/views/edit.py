from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from formlib import Formless
from django import forms
from django.http import HttpResponseRedirect

@view_function
def process_request(request, Product:cmod.Product=None):
    if Product.__class__.__name__ == 'BulkProduct':
        form = EditProductForm(request, initial = {
            'category': Product.category,
            'type': Product.__class__.__name__,
            'name': Product.name,
            'description': Product.description,
            'price': Product.price,
            'status': Product.status,
            'quantity': Product.quantity,
            'reorder_trigger': Product.reorder_trigger,
            'reorder_quantity': Product.reorder_quantity,
        })
    elif Product.__class__.__name__ == 'IndividualProduct':
        form = EditProductForm(request, initial = {
            'category': Product.category,
            'type': Product.__class__.__name__,
            'name': Product.name,
            'description': Product.description,
            'price': Product.price,
            'status': Product.status,
            'itemID': Product.itemID
        })
    elif Product.__class__.__name__ == 'RentalProduct':
        form = EditProductForm(request, initial = {
            'category': Product.category,
            'type': Product.__class__.__name__,
            'name': Product.name,
            'description': Product.description,
            'price': Product.price,
            'status': Product.status,
            'itemID': Product.itemID,
            'maxRental': Product.maxRental,
            'retireDate': Product.retireDate
        })
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/manager/index/')
    context = {
        'product': Product,
        'form': form
    }

    return request.dmp_render('edit.html', context)

class EditProductForm(Formless):
    def init(self):
        STATUS_CHOICES = (
            ('A', 'Active'),
            ('I', 'Inactive')
        )
        self.fields['type'] = forms.ChoiceField(label='Type', choices=cmod.Product.TYPE_CHOICES, required=False)
        self.fields['type'].widget.attrs['disabled'] = True
        self.fields['category'] = forms.ModelChoiceField(queryset=cmod.Category.objects.all(),label='Category')
        self.fields['name'] = forms.CharField(max_length=50, label='Name')
        self.fields['description'] = forms.CharField(max_length=1000, label='Description')
        self.fields['price'] = forms.DecimalField(max_digits=19, decimal_places=2)
        self.fields['status'] = forms.ChoiceField(choices=STATUS_CHOICES)
        self.fields['quantity'] = forms.IntegerField(required=False)
        self.fields['reorder_trigger'] = forms.IntegerField(label='Reorder Trigger', required=False)
        self.fields['reorder_quantity'] = forms.IntegerField(label='Reorder Quantity', required=False)
        self.fields['itemID'] = forms.IntegerField(label='Item ID', required=False)
        self.fields['maxRental'] = forms.IntegerField(label='Max Rental Days', required=False)
        self.fields['retireDate'] = forms.DateTimeField(label='Rental Retire Date', required=False)

    def clean(self):
        if self.cleaned_data.get('type') == 'BulkProduct':
            if self.cleaned_data.get('quantity') is None:
                raise forms.ValidationError('If you create a Bulk Product, you must indicate a quantity')
            if self.cleaned_data.get('reorder_trigger') is None:
                raise forms.ValidationError('If you create a Bulk Product, you must indicate a reorder trigger')
            if self.cleaned_data.get('reorder_quantity') is None:
                raise forms.ValidationError('If you create a Bulk Product, you must indicate a reorder quantity')
        if self.cleaned_data.get('type') == 'IndividualProduct' or self.cleaned_data.get('type') == 'RentalProduct':
            if self.cleaned_data.get('itemID') is None:
                raise forms.ValidationError('If you create an Individual Product or a Rental Product, you must indicate an itemID')
        if self.cleaned_data.get('type') == 'RentalProduct':
            if self.cleaned_data.get('maxRental') is None:
                raise forms.ValidationError('If you create a Rental Product, you must indicate a max rental amount')
            if self.cleaned_data.get('retireDate') is None:
                raise forms.ValidationError('If you create a Rental Product, you must indicate a retire date')

    def commit(self):
        newProduct = cmod.Product.objects.get(id=self.request.urlparams[0])
        if newProduct.__class__.__name__ == 'BulkProduct':
            newProduct.name = self.cleaned_data.get('name')
            newProduct.category = self.cleaned_data.get('category')
            newProduct.description = self.cleaned_data.get('description')
            newProduct.price = self.cleaned_data.get('price')
            newProduct.status = self.cleaned_data.get('status')
            newProduct.quantity = self.cleaned_data.get('quantity')
            newProduct.reorder_trigger = self.cleaned_data.get('reorder_trigger')
            newProduct.reorder_quantity = self.cleaned_data.get('reorder_quantity')
            newProduct.save()
        elif newProduct.__class__.__name__ == 'IndividualProduct':
            newProduct.category = self.cleaned_data.get('category')
            newProduct.name = self.cleaned_data.get('name')
            newProduct.description = self.cleaned_data.get('description')
            newProduct.price = self.cleaned_data.get('price')
            newProduct.status = self.cleaned_data.get('status')
            newProduct.itemID = self.cleaned_data.get('itemID')
            newProduct.save()
        elif newProduct.__class__.__name__ == 'RentalProduct':
            newProduct.category = self.cleaned_data.get('category')
            newProduct.name = self.cleaned_data.get('name')
            newProduct.description = self.cleaned_data.get('description')
            newProduct.price = self.cleaned_data.get('price')
            newProduct.status = self.cleaned_data.get('status')
            newProduct.itemID = self.cleaned_data.get('itemID')
            newProduct.maxRental = self.cleaned_data.get('maxRental')
            newProduct.retireDate = self.cleaned_data.get('retireDate')
            newProduct.save()

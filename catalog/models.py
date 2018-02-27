from django.db import models
from polymorphic.models import PolymorphicModel


class Category(models.Model):
    '''Category for products'''
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(PolymorphicModel):
    ''' A bulk, individual, or rental product'''
    TYPE_CHOICES = (
        ('BulkProduct', 'Bulk Product'),
        ('IndividualProduct', 'Individual Product'),
        ('RentalProduct', 'Rental Product')
    )
    STATUS_CHOICES =(
        ('A', 'Active'),
        ('I', 'Inactive')
    )

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    type = models.TextField(choices=TYPE_CHOICES, default='BulkProduct')
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    status = models.TextField(choices=STATUS_CHOICES, default='A')

    def get_quantity(self):
        return 1


class BulkProduct(Product):
    '''A Bulk Product'''
    TITLE = 'Bulk'
    reorder_trigger = models.IntegerField(default=0, null=True)
    reorder_quantity = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(null=True)

    def get_quantity(self):
        return self.quantity


class IndividualProduct(Product):
    TITLE = 'Individual'


class RentalProduct(Product):
    '''A rental product (Tracked individually)'''
    TITLE = 'Rental'
    itemID = models.TextField(null=True)
    maxRental = models.IntegerField(default=0, null=True)
    retireDate = models.DateField(null=True)

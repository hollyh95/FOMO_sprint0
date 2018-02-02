from django.test import TestCase
# from account import models as amod
from django.contrib.auth.models import Permission, Group, ContentType
from account import models as amod

# Create your tests here.

class UserModelTest(TestCase):

    fixtures = ['fixtures.json']

    def setUp(self):
        self.u1 = amod.User()
        self.u1.first_name= "Marge"
        self.u1.last_name = "Simpson"
        self.u1.email = "marge@simpsons.com"
        self.u1.set_password('password')
        self.u1.save()

    def test_user_create_save_load(self):
        '''Tests round trip of User model data to/from database'''
        u2= amod.User.objects.get(email='marge@simpsons.com')
        self.assertEquals(self.u1.first_name, u2.first_name)
        self.assertEquals(self.u1.last_name, u2.last_name)
        self.assertEquals(self.u1.email, u2.email)
        self.assertEquals(self.u1.set_password, u2.set_password)
        self.assertTrue(u2.check_password('password'))

    def test_add_groups_check_permissions(self):
        for p in Permission.objects.all():
            print(p.content_type.app_label + "." + p.codename)
        p1 = Permission()
        p1.name = 'Change product price'
        p1.codename = 'change_product_price'
        p1.content_type = ContentType.objects.get(id=1)
        p1.save()
        self.u1.user_permissions.add(p1)

    def test_permissions(self):
        g1 = Group()
        g1.name = 'Salespeople'
        g1.save()
        g1.permissions.add(Permission.objects.get(id=4))
        self.u1.groups.add(g1)
        self.u1.save()
        self.assertTrue(self.u1.has_perm('admin.salesperson_permission'))









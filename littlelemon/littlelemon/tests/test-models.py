from django.tests import TestCase
from restaurant.models import Menu 


#TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
        
        
        
class MenuViewTest():
    def setup(self):
       self.menu = Menu('menu')
       
    def test_get_all(self):
        item =Menu.objects.all()
        self.assertEqual(item, Menu)

from django.test import TestCase
from django.urls import reverse

# from ESMarketplace.esm.models import *

# Create your tests here.
class AllViewsTests(TestCase):
    def test_home_page(self):
        self.assertEqual(self.client.get(reverse('esm:home')).status_code, 302)

    def test_login_page(self):
        self.assertEqual(self.client.get(reverse('esm:login')).status_code, 200)

    def test_logout_page(self):
        self.assertEqual(self.client.get(reverse('esm:logout')).status_code, 302)

    def test_signup_page(self):
        self.assertEqual(self.client.get(reverse('esm:signup')).status_code, 200)

    def test_create_page(self):
        self.assertEqual(self.client.get(reverse('esm:create')).status_code, 200)

    def test_store_page(self):
        self.assertEqual(self.client.get(reverse('esm:store')).status_code, 200)

    def test_purchased_page(self):
        self.assertEqual(self.client.get(reverse('esm:purchased')).status_code, 200)

    def test_account_page(self):
        self.assertEqual(self.client.get(reverse('esm:account')).status_code, 200)


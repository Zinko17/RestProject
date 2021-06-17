from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import *
from product.models import Category

class OrderTest(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='aaa',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aaa',email='aa@gmail.com',address='aaa',)
        self.category = Category.objects.create(title='aaa')
        self.product = Product.objects.create(name='aaa',desc='aaa',category=self.category)
        self.url = reverse('order')


    def test_order_post(self):
        self.client.login(username='aaa', password='123456')
        data = {
            "product":1,
            "profile":1,
            "quantity":2
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,201)



    def test_order_bad_request(self):
        self.client.login(username='aaa', password='123456')
        data = {
            "product":1,
            "profile":111,
            "quantity":2
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,400)


    def test_order_product(self):
        self.client.login(username='aaa', password='123456')
        data = {
            "product":111,
            "profile":1,
            "quantity":2
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,400)

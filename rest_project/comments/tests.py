from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from product.models import Category

class CommentTest(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='aaa',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aaa',email='aa@gmail.com',address='aaa',)
        self.category = Category.objects.create(title='aaa')
        self.product = Product.objects.create(name='aaa',desc='aaa',category=self.category)
        self.url = reverse('product_detail', args=(self.product.id,))

    def test_comment_successful(self):
        self.client.login(username='aaa',password='123456')
        data = {
            "text":"good"
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code,201)

    def test_comment_badword(self):
        self.client.login(username='aaa', password='123456')
        data = {
            "text":"bad"
        }
        self.response = self.client.post(self.url,data)
        self.assertContains(self.response,"bad boy",status_code=400)

class RateTest(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='aaa',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aaa',email='aa@gmail.com',address='aaa',)
        self.category = Category.objects.create(title='aaa')
        self.product = Product.objects.create(name='aaa',desc='aaa',category=self.category)
        self.url = reverse('rate', args=(self.product.id,))

    def test_score_create(self):
        self.client.login(username='aaa',password='123456')
        data = {
            "score": 4.1
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code, 201)
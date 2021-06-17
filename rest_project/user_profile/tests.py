from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

class RegisterTest(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('register')

    def test_reg_ok(self):
        data = {
            "username":"111",
            "password":"123456",
            "check_password":"123456",
            "profile":{
            "full_name":"aaa",
            "adress":"aaa",
            "email":"aaa@gmail.com"
            }
            }
        self.response = self.client.post(self.url,data,format='json')
from django.db import models
from user_profile.models import Profile, User
from product.models import Product

class Comment(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
from django.db import models
from user_profile.models import Profile
from product.models import Product

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True)
    quantity = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15,choices=(
        ('in_process','in_process'),
        ('ready','ready'),
        ('received','received')
    ),default='in_process')
    total_sum = models.FloatField(default=0.0)




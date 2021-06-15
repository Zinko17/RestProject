from django.db import models




class Category(models.Model):
    title = models.TextField()


    def __str__(self):
        return self.title



class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    photo = models.ImageField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

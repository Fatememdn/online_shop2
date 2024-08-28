from django.db import models




class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ManyToManyField(Category, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name


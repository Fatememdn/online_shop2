from django.db import models
from accounts.models import User
from products.models import Product

class UserOrder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderDetail', blank= True)
    def __str__(self):
        return f"Order {self.id} by {self.user.name}"

class OrderDetail(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def item_price(self):
        return self.product.price * self.quantity
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"

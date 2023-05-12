from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class Customer(models.Model):
    first_name = models.CharField('First Name', max_length=40)
    middle_name = models.CharField(
        'Middle Name', null=True, blank=True, max_length=40
    )
    last_name = models.CharField('Last Name', max_length=40)
    email = models.EmailField('Email')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField('Name', max_length=40)
    description = models.TextField(
        'Description', null=True, blank=True, max_length=400
    )
    price = models.DecimalField(
        'Price', max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )

    def __str__(self):
        return f'{self.name} {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(
        to=Customer, on_delete=models.CASCADE, verbose_name='Customer'
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, verbose_name='Product'
    )
    quantity = models.IntegerField('Quantity')

    def get_total_cost(self):
        total_cost = self.product.price * self.quantity
        return total_cost

    def __str__(self):
        return f'{self.customer} {self.get_total_cost()}'

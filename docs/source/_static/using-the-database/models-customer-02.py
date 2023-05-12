from django.db import models


class Customer(models.Model):
    first_name = models.CharField('First Name', max_length=40)
    middle_name = models.CharField(
        'Middle Name', null=True, blank=True, max_length=40
    )
    last_name = models.CharField('Last Name', max_length=40)
    email = models.EmailField('Email')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

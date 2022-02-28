from django.db import models
from django.utils import timezone

# Create your models here.


class TransactionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    location = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    update_by = models.CharField(max_length=255)


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # deposit less than a million
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    create_date = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    update_by = models.CharField(max_length=255)
    update_by1 = models.CharField(max_length=255)


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    credit = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    debit = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    create_date = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255)

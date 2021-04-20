from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY = (
        ('Food', 'Food'),
        ('Fun', 'Fun'),
        ('Self-care', 'Self-care'),
        ('Transportation', 'Transportation'),
        ('Culture', 'Culture'),
        ('Household', 'Household'),
        ('Clothes', 'Clothes'),
        ('Beauty', 'Beauty'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Gift', 'Gift'),
        ('Tax','Tax'),
        ('Stocks','Stocks'),
        ('Other', 'Other'),
    )
    TYPE = (
        ('Cash', 'Cash'),
        ('Account', 'Account'),
    )

    cost = models.FloatField(blank=True)
    account = models.CharField(max_length=100, choices=TYPE)
    category = models.CharField(max_length=100, choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

class Income(models.Model):
    CATEGORY = (
        ('Allowance', 'Allowance'),
        ('Salary', 'Salary'),
        ('Cash', 'Cash'),
        ('Bonus', 'Bonus'),
        ('Account', 'Through Account'),
        ('Other', 'Other'),
        
    )

    TYPE = (
        ('Cash', 'Cash'), 
        ('Account', 'Account'),
    )


    cost = models.FloatField(blank=True)
    account = models.CharField(max_length=100, choices=TYPE)
    category = models.CharField(max_length=100, choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

class Transfer(models.Model):
    TYPE = (
        ('Cash', 'Cash'),
        ('Account', 'Account'),
    )

    cost = models.FloatField(blank=True)
    From = models.CharField(max_length=100, choices=TYPE)
    to = models.CharField(max_length=100, choices=TYPE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   


   
    
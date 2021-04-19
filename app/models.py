from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY = (
        ('Food', 'Food'),
        ('Going out/Fun', 'Going out/Fun'),
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
 #       ('Card', 'Card'),
    )

    cost = models.FloatField(blank=True)
    account = models.CharField(max_length=100, choices=TYPE)
    category = models.CharField(max_length=100, choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
#    bookmark = models.BooleanField(default=False)
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
#        ('Card', 'Card'),
    )


    cost = models.FloatField(blank=True)
    account = models.CharField(max_length=100, choices=TYPE)
    category = models.CharField(max_length=100, choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
 #   bookmark = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

class Transfer(models.Model):
    TYPE = (
        ('Cash', 'Cash'),
        ('Account', 'Account'),
#        ('Card', 'Card'),
    )

    cost = models.FloatField(blank=True)
    From = models.CharField(max_length=100, choices=TYPE)
    to = models.CharField(max_length=100, choices=TYPE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
 #   bookmark = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   

'''
class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    title  = models.CharField(max_length=100)
    content = models.CharField(max_length=255)

    def serialize(self,id):

        return {
            "id":id,
            "title":self.title,
            "content":self.content,
            "date":self.date.strftime("%b %Od %Y, %OI:%M %p")
        }
'''
   
    
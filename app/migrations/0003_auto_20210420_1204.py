# Generated by Django 3.1.4 on 2021-04-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210419_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Fun', 'Fun'), ('Self-care', 'Self-care'), ('Transportation', 'Transportation'), ('Culture', 'Culture'), ('Household', 'Household'), ('Clothes', 'Clothes'), ('Beauty', 'Beauty'), ('Health', 'Health'), ('Education', 'Education'), ('Gift', 'Gift'), ('Tax', 'Tax'), ('Stocks', 'Stocks'), ('Other', 'Other')], max_length=100),
        ),
    ]
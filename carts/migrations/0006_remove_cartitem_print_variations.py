# Generated by Django 3.0.5 on 2020-04-28 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_cartitem_print_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='print_variations',
        ),
    ]

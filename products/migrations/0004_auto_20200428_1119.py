# Generated by Django 3.0.5 on 2020-04-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_printpainting_productprint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printpainting',
            old_name='productPrint',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='printpainting',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]

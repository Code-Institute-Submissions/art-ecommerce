# Generated by Django 3.0.5 on 2020-04-24 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OriginalPainting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrintPainting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='img')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.CollectionCategory')),
                ('original_painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.OriginalPainting')),
                ('prints', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.PrintPainting')),
            ],
        ),
    ]

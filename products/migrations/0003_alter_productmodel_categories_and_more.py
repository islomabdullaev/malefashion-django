# Generated by Django 4.2.3 on 2023-07-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productmodel_brand_productmodel_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='categories',
            field=models.ManyToManyField(to='products.categorymodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='colors',
            field=models.ManyToManyField(to='products.colormodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='sizes',
            field=models.ManyToManyField(to='products.sizemodel'),
        ),
    ]

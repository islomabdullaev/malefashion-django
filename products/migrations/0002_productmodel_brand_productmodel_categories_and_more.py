# Generated by Django 4.2.3 on 2023-07-24 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brandmodel', verbose_name='brand'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='categories',
            field=models.ManyToManyField(null=True, to='products.categorymodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='colors',
            field=models.ManyToManyField(null=True, to='products.colormodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='sizes',
            field=models.ManyToManyField(null=True, to='products.sizemodel'),
        ),
    ]

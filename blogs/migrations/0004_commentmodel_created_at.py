# Generated by Django 4.2.3 on 2023-07-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_postmodel_banner_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at'),
        ),
    ]

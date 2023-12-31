# Generated by Django 4.2.3 on 2023-07-10 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('image', models.ImageField(upload_to='image', verbose_name='image')),
                ('banner', models.ImageField(upload_to='banner', verbose_name='image')),
                ('description', models.TextField(verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.authormodel', verbose_name='author')),
                ('tags', models.ManyToManyField(to='blogs.tagmodel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]

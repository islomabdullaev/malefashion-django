# Generated by Django 4.2.3 on 2023-07-14 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_tagmodel_postmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='banner',
            field=models.ImageField(upload_to='banner', verbose_name='banner'),
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('email', models.EmailField(max_length=64, verbose_name='email')),
                ('phone', models.CharField(max_length=13, verbose_name='phone')),
                ('comment', models.TextField(verbose_name='comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.postmodel', verbose_name='comments')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]

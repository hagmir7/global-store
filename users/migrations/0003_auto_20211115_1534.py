# Generated by Django 3.2.9 on 2021-11-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_Profile'),
        ('users', '0002_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='user', null=True, upload_to='avatar/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cover',
            field=models.ImageField(blank=True, default='covare', null=True, upload_to='cover/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='profile_views', to='products.Ipaddrisse'),
        ),
    ]

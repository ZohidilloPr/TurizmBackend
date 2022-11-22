# Generated by Django 4.1.2 on 2022-11-22 04:10

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundimagefornews',
            name='bg_img',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[2500, 1500], upload_to='BackgroundImageForNews/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[2500, 1500], upload_to='posts/'),
        ),
    ]

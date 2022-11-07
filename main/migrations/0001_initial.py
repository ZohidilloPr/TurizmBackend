# Generated by Django 4.1.2 on 2022-11-07 02:38

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uz_name', models.CharField(max_length=200)),
                ('ru_name', models.CharField(blank=True, max_length=200, null=True)),
                ('en_name', models.CharField(blank=True, max_length=200, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('post_view', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_img', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='backgroundImage/')),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundImageForAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_img', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='BackgroundImageForAreas/')),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundImageForNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_img', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='BackgroundImageForNews/')),
            ],
        ),
        migrations.CreateModel(
            name='NavbarName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uz_name', models.CharField(max_length=200)),
                ('ru_name', models.CharField(blank=True, max_length=200, null=True)),
                ('en_name', models.CharField(blank=True, max_length=200, null=True)),
                ('navbar_img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='navbarname/')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoArxiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='photoArxiv/')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_img', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='posts/')),
                ('uz_title', models.CharField(max_length=200)),
                ('ru_title', models.CharField(blank=True, max_length=200, null=True)),
                ('en_title', models.CharField(blank=True, max_length=200, null=True)),
                ('uz_description', models.CharField(max_length=100)),
                ('ru_description', models.CharField(blank=True, max_length=200, null=True)),
                ('en_description', models.CharField(blank=True, max_length=200, null=True)),
                ('uz_post', ckeditor_uploader.fields.RichTextUploadingField()),
                ('ru_post', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('en_post', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('post_view', models.IntegerField(blank=True, default=0, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoArxiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foster', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='video_fosters/')),
                ('video', models.FileField(upload_to='videos/')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderSlider',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.post')),
            ],
            bases=('main.post',),
        ),
        migrations.CreateModel(
            name='NavbarItems',
            fields=[
                ('autodate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.autodate')),
                ('navbar_img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='navbaritems/')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('navbar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.navbarname')),
            ],
            bases=('main.autodate',),
        ),
        migrations.CreateModel(
            name='WebSiteName',
            fields=[
                ('autodate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.autodate')),
                ('logo', django_resized.forms.ResizedImageField(crop=None, default='default/logo.png', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='logo/')),
            ],
            bases=('main.autodate',),
        ),
        migrations.AddField(
            model_name='post',
            name='navbaritem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.navbaritems'),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.post')),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.navbarname')),
            ],
            bases=('main.post',),
        ),
        migrations.CreateModel(
            name='Hududlar',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.post')),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.navbarname')),
            ],
            bases=('main.post',),
        ),
    ]

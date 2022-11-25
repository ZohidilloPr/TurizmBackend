# Generated by Django 4.1.2 on 2022-11-24 11:48

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_backgroundimage_bg_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(help_text="Sarlovha matning o'zbekcha talqini", max_length=200, verbose_name='Sarlovha')),
                ('title_ru', models.CharField(help_text='Sarlovha matning rus tilidagi talqini', max_length=200, verbose_name='Sarlovha')),
                ('title_en', models.CharField(help_text='Sarlovha matning ingiliz tilidagi talqini', max_length=200, verbose_name='Sarlovha')),
                ('post_uz', ckeditor_uploader.fields.RichTextUploadingField()),
                ('post_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('post_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('post_view', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('navbar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.navbarname')),
            ],
            options={
                'verbose_name': 'Biz xaqimizda',
                'verbose_name_plural': 'Biz xaqimizda',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(help_text="Sarlovha matning o'zbekcha talqini", max_length=200, verbose_name='Sarlovha')),
                ('title_ru', models.CharField(help_text='Sarlovha matning rus tilidagi talqini', max_length=200, verbose_name='Sarlovha')),
                ('title_en', models.CharField(help_text='Sarlovha matning ingiliz tilidagi talqini', max_length=200, verbose_name='Sarlovha')),
                ('post_uz', ckeditor_uploader.fields.RichTextUploadingField()),
                ('post_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('post_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('post_view', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('navbar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.navbarname')),
            ],
            options={
                'verbose_name': 'Biz xaqimizda',
                'verbose_name_plural': 'Biz xaqimizda',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
# Generated by Django 4.1.2 on 2022-11-04 06:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_post_en_post_alter_post_ru_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uz_post',
            field=ckeditor.fields.RichTextField(verbose_name='uz_post'),
        ),
    ]

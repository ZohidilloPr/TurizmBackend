# Generated by Django 4.1.2 on 2022-10-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_websitename_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autodate',
            name='post_view',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='navbarname',
            name='post_view',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

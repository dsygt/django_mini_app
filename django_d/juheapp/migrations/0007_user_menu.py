# Generated by Django 2.2.8 on 2020-03-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juheapp', '0006_auto_20200309_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='menu',
            field=models.ManyToManyField(to='juheapp.App'),
        ),
    ]

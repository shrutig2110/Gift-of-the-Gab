# Generated by Django 3.2.2 on 2021-06-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='thumbnail',
            field=models.URLField(default='', max_length=500),
        ),
    ]

# Generated by Django 3.2 on 2021-07-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20210723_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]

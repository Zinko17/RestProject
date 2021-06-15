# Generated by Django 3.2.4 on 2021-06-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_profile_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='order_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sale',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wallet',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avg_score',
            field=models.FloatField(default=0.0),
        ),
    ]

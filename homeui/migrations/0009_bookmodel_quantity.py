# Generated by Django 4.1.1 on 2024-02-21 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeui', '0008_alter_bookmodel_bookprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]

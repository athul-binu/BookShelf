# Generated by Django 4.1.1 on 2024-02-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookprice',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

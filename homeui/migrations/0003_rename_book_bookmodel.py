# Generated by Django 4.1.1 on 2024-02-16 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeui', '0002_book_bookprice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='book',
            new_name='bookmodel',
        ),
    ]

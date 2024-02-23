# Generated by Django 4.1.1 on 2024-02-23 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeui', '0014_alter_bookmodel_book_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartmodel',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeui.bookmodel')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeui.usermodel')),
            ],
        ),
    ]
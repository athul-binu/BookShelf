# Generated by Django 4.1.1 on 2024-02-19 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeui', '0006_alter_category_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writereview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_des', models.TextField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeui.bookmodel')),
            ],
            options={
                'db_table': 'review_table',
            },
        ),
    ]

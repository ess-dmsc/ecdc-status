# Generated by Django 3.0.2 on 2020-01-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxim',
            name='Text',
            field=models.TextField(max_length=2000),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ComputerDetail',
        ),
    ]
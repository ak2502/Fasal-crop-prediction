# Generated by Django 3.1.4 on 2020-12-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soil',
            name='soil_type',
            field=models.CharField(choices=[('Black', 'black soil'), ('Alluvial', 'alluvial soil'), ('Loamy', 'loamy soil'), ('Red', 'red soil')], max_length=8),
        ),
    ]
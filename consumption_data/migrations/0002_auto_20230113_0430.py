# Generated by Django 3.1.3 on 2023-01-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumption_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='energy_consumption',
            name='consume',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='energy_consumption',
            name='house_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='energy_consumption',
            name='user_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='energy_consumption',
            name='user_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

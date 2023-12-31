# Generated by Django 4.2.3 on 2023-08-24 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_alter_mileage_motorcycle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mileage',
            options={'ordering': ('-year',), 'verbose_name': 'пробег', 'verbose_name_plural': 'пробеги'},
        ),
        migrations.AlterField(
            model_name='mileage',
            name='motorcycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.motorcycle'),
        ),
    ]

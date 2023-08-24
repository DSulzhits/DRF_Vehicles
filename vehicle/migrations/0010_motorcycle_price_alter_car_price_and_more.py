# Generated by Django 4.2.4 on 2023-08-24 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0009_alter_mileage_options_alter_mileage_motorcycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycle',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='mileage',
            name='motorcycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mileage', to='vehicle.motorcycle'),
        ),
    ]
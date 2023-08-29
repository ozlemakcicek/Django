# Generated by Django 4.2.4 on 2023-08-21 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_reservation_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='flights.flight'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ManyToManyField(related_name='reservation', to='flights.passenger'),
        ),
    ]
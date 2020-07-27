# Generated by Django 2.2.5 on 2020-06-23 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BusBooking', '0007_auto_20200623_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bus_number', models.IntegerField()),
                ('Start_time', models.TimeField()),
                ('Total_seats', models.IntegerField()),
                ('Route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusBooking.AddRouteModel')),
            ],
        ),
    ]
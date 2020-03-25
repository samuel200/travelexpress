# Generated by Django 2.2 on 2020-03-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('terminal', models.CharField(max_length=2)),
                ('gate', models.IntegerField()),
                ('departure_time', models.DateTimeField()),
                ('airport', models.CharField(max_length=200)),
                ('flight_class', models.CharField(max_length=50)),
                ('seat_number', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
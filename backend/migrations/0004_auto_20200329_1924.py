# Generated by Django 3.0.4 on 2020-03-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200329_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='depart_from',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(max_length=200),
        ),
    ]
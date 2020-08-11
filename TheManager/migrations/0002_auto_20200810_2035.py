# Generated by Django 3.1 on 2020-08-10 20:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TheManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtransactions',
            name='DateOfPayment',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 20, 35, 29, 42710, tzinfo=utc), verbose_name='Payment Date'),
        ),
        migrations.AlterField(
            model_name='subproperty',
            name='EffectiveDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 20, 35, 29, 39565, tzinfo=utc), verbose_name='When Property was given out'),
        ),
        migrations.AlterField(
            model_name='subproperty',
            name='ExpiryDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 20, 35, 29, 39602, tzinfo=utc), verbose_name='Rent Expiry Date'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='FirstEngagementDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 20, 35, 29, 40744, tzinfo=utc), verbose_name='Date Property was given out'),
        ),
    ]

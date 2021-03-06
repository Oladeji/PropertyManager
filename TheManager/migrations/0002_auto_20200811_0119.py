# Generated by Django 3.1 on 2020-08-11 01:19

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
            field=models.DateField(default=datetime.datetime(2020, 8, 11, 1, 19, 1, 67795, tzinfo=utc), verbose_name='Payment Date'),
        ),
        migrations.AlterField(
            model_name='subproperty',
            name='EffectiveDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 11, 1, 19, 1, 64565, tzinfo=utc), verbose_name='WHEN THE PROPERTY WAS GIVEN OUT(Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='subproperty',
            name='ExpiryDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 11, 1, 19, 1, 64604, tzinfo=utc), verbose_name='RENT EXPIRY DATE(Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='FirstEngagementDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 11, 1, 19, 1, 65715, tzinfo=utc), verbose_name='DATE PROPERTY WAS FIRST GIVEN OUT'),
        ),
    ]

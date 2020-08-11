# Generated by Django 3.1 on 2020-08-10 23:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TheManager', '0002_auto_20200810_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='PaymentState',
            field=models.CharField(default='YET TO BALANCE UP', max_length=20, verbose_name='BALANCE (Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='detailtransactions',
            name='DateOfPayment',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 23, 36, 13, 583051, tzinfo=utc), verbose_name='Payment Date'),
        ),
        migrations.AlterField(
            model_name='periodicrenttransactions',
            name='AmountPaidSofar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='AMOUNT PAID SO FAR (Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='periodicrenttransactions',
            name='AmountToBalance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='REMAINING BALANCE (Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='periodicrenttransactions',
            name='CurrentRunningPeriod',
            field=models.CharField(max_length=50, verbose_name='PERIOD OF RENT'),
        ),
        migrations.AlterField(
            model_name='periodicrenttransactions',
            name='RentRate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='RENT RATE (Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='subproperty',
            name='EffectiveDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 23, 36, 13, 579795, tzinfo=utc), verbose_name='When Property was given out'),
        ),
        migrations.AlterField(
            model_name='subproperty',
            name='ExpiryDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 23, 36, 13, 579831, tzinfo=utc), verbose_name='Rent Expiry Date'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='AmountPaidSofar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='AMOUNT PAID SO FAR (Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='AmountToBalance',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='BALANCE (Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='CurrentRentRate',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='TOTAL AMOUNT FOR PERIOD (Auto Fill)'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='CurrentRunningPeriod',
            field=models.CharField(max_length=50, verbose_name='PERIOD OF RENT'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='FirstEngagementDate',
            field=models.DateField(default=datetime.datetime(2020, 8, 10, 23, 36, 13, 580957, tzinfo=utc), verbose_name='DATE PROPERTY WAS FIRST GIVEN OUT'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='OccupantPhoneNo',
            field=models.CharField(max_length=100, verbose_name='PHONE NO'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='OccupantRefDetails',
            field=models.CharField(max_length=100, verbose_name='REFEREE INFORMATION'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='PresentOccupant',
            field=models.CharField(max_length=100, verbose_name='FULL NAME'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='Referee',
            field=models.CharField(max_length=100, verbose_name='REFEREE NAME'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='TenantPhoto',
            field=models.ImageField(upload_to='TenantPhotos', verbose_name='PASSPORT PHOTO'),
        ),
    ]

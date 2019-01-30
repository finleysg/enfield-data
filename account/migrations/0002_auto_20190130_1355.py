# Generated by Django 2.1.5 on 2019-01-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='address_txt',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='historicalaccount',
            old_name='address_txt',
            new_name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='alternate_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Alternate Phone'),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='contact',
            name='fax',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Fax'),
        ),
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='contact',
            name='primary_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Primary Phone'),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='alternate_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Alternate Phone'),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='fax',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Fax'),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='historicalcontact',
            name='primary_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Primary Phone'),
        ),
    ]

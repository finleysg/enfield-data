# Generated by Django 2.1.5 on 2019-02-23 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=10, unique=True, verbose_name='Account Number')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=40, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, default='TN', max_length=2, null=True, verbose_name='State')),
                ('zip', models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip Code')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'ordering': ['account_type__description', 'name'],
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=30, verbose_name='Description')),
                ('tax_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=5, verbose_name='Tax Rate')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Account Type',
                'verbose_name_plural': 'Account Types',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('first_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('primary_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Primary Phone')),
                ('alternate_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Alternate Phone')),
                ('fax', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fax')),
                ('do_notify', models.BooleanField(default=False, verbose_name='Notification Flag')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account', verbose_name='Account')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalAccount',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('account_number', models.CharField(db_index=True, max_length=10, verbose_name='Account Number')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=40, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, default='TN', max_length=2, null=True, verbose_name='State')),
                ('zip', models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip Code')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('account_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='account.AccountType', verbose_name='Account Type')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical account',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAccountType',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=30, verbose_name='Description')),
                ('tax_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=5, verbose_name='Tax Rate')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Account Type',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalContact',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('first_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('primary_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Primary Phone')),
                ('alternate_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Alternate Phone')),
                ('fax', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fax')),
                ('do_notify', models.BooleanField(default=False, verbose_name='Notification Flag')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('account', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='account.Account', verbose_name='Account')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical contact',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.AccountType', verbose_name='Account Type'),
        ),
    ]

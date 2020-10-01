# Generated by Django 3.0.7 on 2020-09-20 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.IntegerField(verbose_name='Loan Amount')),
                ('loan_balance', models.IntegerField(null=True, verbose_name='Loan Amount')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Staff')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField(verbose_name='Amount Paid')),
                ('bal_left', models.IntegerField(verbose_name='Balance Outstanding')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField(default=django.utils.timezone.now)),
                ('loan_amount', models.IntegerField(verbose_name='Loan Amount')),
                ('status', models.CharField(choices=[('PE', 'PE'), ('AC', 'AC'), ('CL', 'CL'), ('AP', 'AP')], max_length=2)),
                ('approved_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by', to='staff.Staff')),
                ('closed_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='closed_by', to='staff.Staff')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
    ]

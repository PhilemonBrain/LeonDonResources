# Generated by Django 3.0.7 on 2020-09-20 11:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('len_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to='len_admin.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('position', models.CharField(default='Manager', max_length=255, verbose_name='Position')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('add_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='len_admin.Admin')),
                ('branch', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='staff.Branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
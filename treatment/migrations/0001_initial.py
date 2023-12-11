# Generated by Django 4.2.6 on 2023-10-24 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatmentstatus', models.CharField(max_length=100)),
                ('statuspayment', models.CharField(max_length=100)),
                ('interventions', models.TextField()),
                ('treatmentamount', models.PositiveIntegerField()),
                ('partpatient', models.PositiveIntegerField()),
                ('partinsurance', models.PositiveIntegerField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-registered_on'],
            },
        ),
    ]

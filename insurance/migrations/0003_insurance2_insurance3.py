# Generated by Django 4.2.6 on 2023-12-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_remove_insurance_id_alter_insurance_insurancename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance2',
            fields=[
                ('insurancename', models.CharField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Insurance3',
            fields=[
                ('insurancename', models.CharField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0003_alter_treatment_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='registered_on',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

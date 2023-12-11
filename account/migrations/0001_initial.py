# Generated by Django 4.2.6 on 2023-10-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('ACCOUNTANT', 'Accountant'), ('DOCTOR', 'Doctor'), ('CASHIER', 'Cashier'), ('PATIENT', 'Patient')], default='ADMIN', max_length=15)),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_accountant', models.BooleanField(default=False)),
                ('is_cashier', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=50)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMELE', 'Femele'), ('OTHER', 'Autre')], max_length=15)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Accountant',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.useraccount',),
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.useraccount',),
        ),
        migrations.CreateModel(
            name='Cashier',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.useraccount',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.useraccount',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.useraccount',),
        ),
    ]
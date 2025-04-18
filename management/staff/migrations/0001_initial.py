# Generated by Django 4.2.20 on 2025-03-12 16:46

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN', unique=True, verbose_name='Mobile Number')),
                ('department', models.CharField(max_length=50, verbose_name='Department')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
            ],
        ),
    ]

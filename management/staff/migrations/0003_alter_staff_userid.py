# Generated by Django 4.2.20 on 2025-03-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staff_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='userId',
            field=models.CharField(max_length=50, verbose_name='User_Id'),
        ),
    ]

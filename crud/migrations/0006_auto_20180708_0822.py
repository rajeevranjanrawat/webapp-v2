# Generated by Django 2.0.4 on 2018-07-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20180626_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 3.0.7 on 2020-09-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects_and_exams', '0004_auto_20200913_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='class_name',
            field=models.IntegerField(choices=[(2, '10')], null=True),
        ),
    ]

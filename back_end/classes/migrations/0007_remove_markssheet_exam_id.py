# Generated by Django 3.0.7 on 2020-09-10 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_remove_exam_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='markssheet',
            name='exam_id',
        ),
    ]
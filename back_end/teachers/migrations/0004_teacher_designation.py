# Generated by Django 3.0.7 on 2020-09-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_remove_teacher_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
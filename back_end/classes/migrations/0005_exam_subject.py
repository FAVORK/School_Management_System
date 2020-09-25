# Generated by Django 3.0.7 on 2020-09-10 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200910_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(blank=True, choices=[(2, 'English')], null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Subject'),
        ),
    ]
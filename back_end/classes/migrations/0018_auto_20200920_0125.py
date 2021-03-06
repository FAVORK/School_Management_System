# Generated by Django 3.0.7 on 2020-09-20 01:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20200920_0059'),
        ('teachers', '0004_teacher_designation'),
        ('classes', '0017_auto_20200914_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('exam_year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(9999)])),
                ('subjective_marks', models.IntegerField()),
                ('objective_marks', models.IntegerField()),
                ('total_marks', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='class',
            name='class_teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('related_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Class')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='MarksSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjective_marks', models.IntegerField()),
                ('objective_marks', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('letter_grade', models.CharField(max_length=5)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Exam')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='related_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Class'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(blank=True, limit_choices_to={'related_class': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Class')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Subject'),
        ),
    ]

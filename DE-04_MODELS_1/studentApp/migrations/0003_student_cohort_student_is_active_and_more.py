# Generated by Django 4.2.3 on 2023-07-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0002_alter_student_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cohort',
            field=models.CharField(choices=[('FS', 'Fullstack'), ('DS', 'DataScience'), ('AWS', 'AWS Devops')], default='FS', max_length=3),
        ),
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

# Generated by Django 2.0.6 on 2018-09-05 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]

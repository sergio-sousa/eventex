# Generated by Django 2.0.6 on 2018-09-06 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_course_abc_to_mti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseold',
            name='speakers',
        ),
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]

# Generated by Django 4.0 on 2023-12-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsdata',
            name='location',
            field=models.CharField(default='Hyd', max_length=50),
        ),
    ]

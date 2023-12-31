# Generated by Django 4.0 on 2023-12-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('fee', models.IntegerField()),
                ('assignment1', models.IntegerField()),
                ('assignment2', models.IntegerField()),
                ('assignment3', models.IntegerField()),
                ('assignment4', models.IntegerField()),
            ],
        ),
    ]

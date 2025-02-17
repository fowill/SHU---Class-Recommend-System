# Generated by Django 3.0.4 on 2021-02-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_id', models.CharField(max_length=128, unique=True)),
                ('student_id', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('school', models.CharField(max_length=256)),
                ('gpa', models.CharField(max_length=256)),
                ('score', models.CharField(max_length=256)),
                ('gpa_lessons', models.CharField(max_length=256)),
                ('gpa_reasons', models.CharField(max_length=256)),
                ('score_lessons', models.CharField(max_length=256)),
                ('score_reasons', models.CharField(max_length=256)),
            ],
        ),
    ]

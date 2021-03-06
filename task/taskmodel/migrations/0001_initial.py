# Generated by Django 3.2 on 2021-05-11 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('noteid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField(max_length=20)),
                ('note', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('scheduleid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField(max_length=20)),
                ('scheduletime', models.DateField(auto_now_add=True)),
                ('scheduleevent', models.CharField(max_length=1000)),
                ('done', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('age', models.DateField(auto_now_add=True)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
            ],
        ),
    ]

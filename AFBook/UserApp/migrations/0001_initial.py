# Generated by Django 4.0.2 on 2022-02-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('StyleId', models.AutoField(primary_key=True, serialize=False)),
                ('StyleName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserUserName', models.CharField(max_length=100)),
                ('UserFirstName', models.CharField(max_length=100)),
                ('UserLastName', models.CharField(max_length=100)),
                ('DateOfBirth', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=100)),
            ],
        ),
    ]

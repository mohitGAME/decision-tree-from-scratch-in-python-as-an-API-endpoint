# Generated by Django 3.0.3 on 2020-05-29 19:55

import classifiy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', validators=[classifiy.models.validate_file_extension])),
                ('classColumn', models.CharField(max_length=30)),
                ('algorithm', models.CharField(max_length=40)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MlModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ColumnName', models.CharField(max_length=100)),
                ('ColumnType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=100)),
                ('Salary', models.IntegerField()),
            ],
        ),
    ]

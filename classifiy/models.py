from django.db import models
from rest_framework import serializers


class PurchaseDetail(models.Model):
    Age = models.IntegerField()
    Gender = models.CharField(max_length=100)
    Salary = models.IntegerField()


def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise serializers.ValidationError("Only CSV file is accepted")


class File(models.Model):
    file = models.FileField(blank=False, null=False, validators=[
                            validate_file_extension])
    classColumn = models.CharField(max_length=30)
    algorithm = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)


class MlModels(models.Model):
    ColumnName = models.CharField(max_length=100)
    ColumnType = models.CharField(max_length=100)

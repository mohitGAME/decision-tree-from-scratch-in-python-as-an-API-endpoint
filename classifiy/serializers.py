from rest_framework import serializers
from .models import PurchaseDetail
from .models import File , MlModels


class PurchaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetail
        fields = ['Age', 'Gender', 'Salary']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class MlSerial(serializers.ModelSerializer):
    class Meta:
        model = MlModels
        fields = "__all__"

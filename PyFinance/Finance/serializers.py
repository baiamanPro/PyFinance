from rest_framework import serializers
from .models import Category, Transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    def validate(self, data):
        if data["amount"] <= 0:
            raise serializers.ValidationError("Сумма должна быть больше 0")

        if data["type"] != data["category"].type:
            raise serializers.ValidationError("Типы не совпадают")

        return data
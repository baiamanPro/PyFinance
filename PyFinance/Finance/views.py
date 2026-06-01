from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    list=extend_schema(tags=["📁 Категории"]),
    retrieve=extend_schema(tags=["📁 Категории"]),
    create=extend_schema(tags=["📁 Категории"]),
    update=extend_schema(tags=["📁 Категории"]),
    partial_update=extend_schema(tags=["📁 Категории"]),
    destroy=extend_schema(tags=["📁 Категории"]),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    http_method_names = ["get", "post", "delete"]

@extend_schema_view(
    list=extend_schema(tags=["💸 Транзакции"]),
    retrieve=extend_schema(tags=["💸 Транзакции"]),
    create=extend_schema(tags=["💸 Транзакции"]),
    update=extend_schema(tags=["💸 Транзакции"]),
    partial_update=extend_schema(tags=["💸 Транзакции"]),
    destroy=extend_schema(tags=["💸 Транзакции"]),
)
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    http_method_names = ["get", "post", "delete"]


@extend_schema(
    tags=["📊 Статистика"],
    description="Баланс, доходы и расходы"
)
class StatisticsAPIView(APIView):
    def get(self, request):
        income = Transaction.objects.filter(type="income").aggregate(Sum("amount"))["amount__sum"] or 0
        expense = Transaction.objects.filter(type="expense").aggregate(Sum("amount"))["amount__sum"] or 0

        return Response({
            "total_income": income,
            "total_expense": expense,
            "balance": income - expense
        })
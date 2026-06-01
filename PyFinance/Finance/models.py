from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    transaction_date = models.DateField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-transaction_date"]
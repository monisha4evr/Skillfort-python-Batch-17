from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=250)
    price=models.DecimalField( max_digits=10, decimal_places=2)
    description=models.CharField(max_length=250,null=True)
    rating=models.IntegerField(max_length=5)
    active_status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name;
    
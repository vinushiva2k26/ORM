from django.db import models

class FoodOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=20)
    restaurant_name = models.CharField(max_length=20)
    order_status = models.CharField(max_length=20)
    food_name = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()

# Create your models here.

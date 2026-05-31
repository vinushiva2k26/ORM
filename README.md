# Ex01 Django ORM Web Application
# Date:
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM

```
(models.py)

from django.db import models

class FoodOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=20)
    restaurant_name = models.CharField(max_length=20)
    order_status = models.CharField(max_length=20)
    food_name = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()

(admin.py)

from django.contrib import admin
from .models import FoodOrder

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):

    list_display = (
        'order_id',
        'customer_name',
        'restaurant_name',
        'order_status',
        'food_name',
        'price',
        'quantity'

    )
```
# OUTPUT

![Output](Screenshot%202026-05-31%20212713.png)


# RESULT
Thus the program for creating a database using ORM hass been executed successfully

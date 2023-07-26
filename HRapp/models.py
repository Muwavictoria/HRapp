from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
User = get_user_model()

availability_choices = (
    ("Available", "Available"),
    ("Unvailable", "Unvailable"),
    ("No longer available", "Suspended"),
)


# Create your models here.
class Menu(models.Model):
    status = models.CharField(
        max_length=50,
        choices=availability_choices,
        default="Unvailable"
    )
    image = models.ImageField(
        upload_to="images/menus",
        default=""
    )


class Table(models.Model):
    table_number = models.IntegerField()


# class CustomUser(AbstractUser):
#     name = models.CharField(
#         max_length=100
#     )
#     contact = models.CharField(
#         max_length=10
#     )




class Order(models.Model):
    name = models.CharField(
        max_length=100
    )
    contact = models.CharField(
        max_length=10
    )
    total_cost = models.IntegerField(
        default=0
    )


class Dishes(models.Model):
    dish_name: CharField = models.CharField(
        max_length=50
    )
    dish_status = models.BooleanField()
    dish_image = models.ImageField(
        upload_to="images/dishes"
    )
    dish_price = models.IntegerField(
        default=0
    )


class Feedback(models.Model):
    feedback_details = models.TextField()


class dish_feedback(models.Model):
    dish_ratings = models.CharField(
        max_length=5
    )
    review_details = models.TextField()

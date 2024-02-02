from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField("Phone", max_length=13, unique=True)
    verification_code = models.CharField("Verification code", max_length=8)
    height = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    day_limit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username


class Food(models.Model):
    VOLUME = (
        ("dona","dona"),
        ("pors","pors"),
        ("100 gram","100 gram"),
    )
    adder = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="foods" )
    title = models.CharField("Nomi", max_length=55)
    volume = models.CharField("Hajmi", max_length=25, choices=VOLUME)
    kkl = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class History(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history")
    foods = models.ManyToManyField(Food)
    kkl = models.PositiveIntegerField(default=0)
    food_volumes = models.JSONField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{ self.user} - {str(self.date)}"



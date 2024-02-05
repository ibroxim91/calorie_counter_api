from main.models import Food
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    adder = serializers.StringRelatedField()
    class Meta:
        model = Food
        fields = "__all__"


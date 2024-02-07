from main.models import History,Food
from rest_framework import serializers



class HistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = History
        exclude = ("foods",) 

class HistoryAddSerializer(serializers.Serializer):
    food = serializers.IntegerField()
    volume = serializers.CharField(max_length=15)

    def validate_food(self,food, *args, **kwargs):
        if type(food) != int:
            raise serializers.ValidationError("food must be integer") 
        if not Food.objects.filter(id=int(food)).exists():
            raise serializers.ValidationError("Food object not found") 
        return food





from rest_framework import serializers
from .models import *

class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Engineer
        fields='__all__'
class Cement_SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model=Cement_Supply
        fields='__all__'


class Water_SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model=Water_Supply
        fields='__all__'
class Brick_SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model=Brick_Supply
        fields='__all__'

class ConstructionSerializer(serializers.ModelSerializer):
    cement_supplies=Cement_SupplySerializer(many=True, read_only=False)
    water_supplies=Water_SupplySerializer(many=True, read_only=True)
    brick_supplies=Brick_SupplySerializer(many=True, read_only=True)

    class Meta:
        model=Construction
        fields=['name','shape','area','num_of_required_col','num_of_finished_col',
                'cement_supplies','water_supplies','brick_supplies']

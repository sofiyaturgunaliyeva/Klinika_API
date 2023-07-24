from rest_framework import serializers

from .models import *

class BemorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bemor
        fields = '__all__'

class YollanmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yollanma
        fields = '__all__'

class XonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xona
        fields = '__all__'

class JoylashtirishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joylashtirish
        fields = '__all__'

class TolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tolov
        fields = '__all__'

class XulosaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xulosa
        fields = '__all__'

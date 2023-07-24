from django.shortcuts import render

from django.shortcuts import render
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status, filters

from rest_framework.viewsets import ModelViewSet


class BemorModelViewSet(ModelViewSet):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer


class XonalarAPIView(APIView):
    def get(self, request):
        xonalar = Xona.objects.all()
        serializer = XonaSerializer(xonalar, many=True)
        return Response(serializer.data)

class BoshXonalarAPIView(APIView):
    def get(self, request):
        bosh_xonalar = Xona.objects.filter(bosh_joy_soni__gt=0)
        serializer = XonaSerializer(bosh_xonalar, many=True)
        return Response(serializer.data)


class JoylashtirishModelViewSet(ModelViewSet):
    queryset = Joylashtirish.objects.all()
    serializer_class = JoylashtirishSerializer

class TolovlarAPIView(APIView):
    def get(self, request):
        tolovlar = Tolov.objects.all()
        serializer = TolovSerializer(tolovlar, many=True)
        return Response(serializer.data)

class BemorTolovlarAPIView(APIView):
    def get(self, request, pk):
        bemor = Bemor.objects.get(pk=pk)
        tolovlar = Tolov.objects.filter(bemor=bemor)
        serializer = TolovSerializer(tolovlar, many=True)
        return Response(serializer.data)


class TolanmaganTolovlarAPIView(APIView):
    def get(self, request):
        tolanmagan_tolovlar = Tolov.objects.filter(tolandi=False)
        serializer = TolovSerializer(tolanmagan_tolovlar, many=True)
        return Response(serializer.data)


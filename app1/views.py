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


    def list(self, request, *args, **kwargs):
        soz = request.query_params.get("qidiruv")
        queryset = Bemor.objects.all()
        if soz:
            queryset = Bemor.objects.filter(ism__contains=soz)
        serializer = BemorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BemorSerializer(data=request.data)
        if serializer.is_valid():
            ism = request.data.get("ism")
            b = Bemor.objects.filter(ism = ism)
            if len(b) == 0:
                serializer.save()
                return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class XonalarAPIView(APIView):
    def get(self, request):
        xonalar = Xona.objects.all()
        serializer = XonaSerializer(xonalar, many=True)
        return Response(serializer.data)

class BoshXonalarAPIView(APIView):
    def get(self, request):
        soz = request.query_params.get("qidiruv")
        if soz == "True":
            xonalar = Xona.objects.filter(bosh_joy_soni__gt=1)
        else:
            xonalar = Xona.objects.filter(bosh_joy_soni__gt=0)
        serializer = XonaSerializer(xonalar, many=True)
        return Response(serializer.data)


class JoylashtirishModelViewSet(ModelViewSet):
    queryset = Joylashtirish.objects.all()
    serializer_class = JoylashtirishSerializer

    # Vazifa:
    #
    # 1.  Joylashtirish uchun patch metod yozing.
    # Shu joylashtirishga tegishli xona bo'sh joylari soniga kerakli miqdorni qo'shib qo'ying.

    def create(self, request, *args, **kwargs):
        serializer = JoylashtirishSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.is_valid():
                serializer.save()
                xona = Xona.objects.get(id = request.data.get('xona'))
                if request.data.get("qarovchi") == True:
                    xona.bosh_joy_soni -= 2
                else:
                    xona.bosh_joy_soni -= 1
                xona.save()
                joylash = Joylashtirish.objects.get(id = serializer.data.get('id'))
                Tolov.objects.create(
                    bemor = Bemor.objects.get(id = serializer.initial_data.get('bemor')),
                    joylashtirish = joylash,
                    sana = serializer.data.get("kelgan_sana"),
                    summa = xona.narx * (joylash.yotgan_kun_soni + 1)
                )
                return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        joylashtirish = Joylashtirish.objects.get(id=pk)
        serializer = JoylashtirishSerializer(joylashtirish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data.get("qarovchi") == True:
                xona = joylashtirish.xona
                xona.bosh_joy_soni += 2
                xona.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TolovlarAPIView(APIView):
    def get(self, request):
        tolovlar = Tolov.objects.all()
        serializer = TolovSerializer(tolovlar, many=True)
        return Response(serializer.data)

class YollanmalarAPIView(APIView):
    def get(self, request):
        tolovlar = Tolov.objects.all()
        serializer = TolovSerializer(tolovlar, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TolovSerializer(data = request.data)
        s = 0
        hisob = Yollanma.objects.get(id = request.data.get('yollanma')).narx
        for i in request.data.get('tolamgan_sana'):
            s += i.get('summa')
        if s == hisob:
            natija = True
        else:
            natija = False
        if serializer.is_valid():
            serializer.save(
                summa = hisob,
                tolandi = natija
            )
            return Response(serializer.data)
        return Response(serializer.errors)
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

class TolovDetailView(APIView):
    def patch(self,request,pk):
        tolov = Tolov.objects.get(id = pk)
        serializer = TolovSerializer(tolov,data = request.data)
        s = 0
        for i in request.data.get('tolangan_summa'):
            s += i.get('summa')
        if s == tolov.summa:
            natija = True
        else:
            natija = False
        if serializer.is_valid():
            serializer.save(tolandi = natija)
            return Response(serializer.data)
        return Response(serializer.errors)




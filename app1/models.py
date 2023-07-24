from django.db import models

class Bemor(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    pasport_ser = models.CharField(max_length=50)

    def __str__(self):
        return self.ism

class Yollanma(models.Model):
    nom = models.CharField(max_length=50)
    xona = models.PositiveSmallIntegerField()
    narx = models.FloatField()

    def __str__(self):
        return self.nom

class Xona(models.Model):
    qavat = models.CharField(max_length=50)
    raqam = models.PositiveSmallIntegerField()
    narx = models.FloatField()
    bosh_joy_soni = models.PositiveSmallIntegerField()
    sigim = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.qavat

class Joylashtirish(models.Model):
    bemor = models.ForeignKey(Bemor,on_delete=models.CASCADE)
    xona = models.ForeignKey(Xona,on_delete=models.CASCADE)
    kelgan_sana = models.DateField()
    ketish_sana = models.DateField(null=True,blank=True)
    yotgan_kun_soni = models.PositiveSmallIntegerField(default=1)
    qarovchi = models.BooleanField(default=False)

    def __str__(self):
        return self.bemor.ism

class Tolov(models.Model):
    bemor = models.ForeignKey(Bemor, on_delete=models.CASCADE)
    yollanma = models.ForeignKey(Yollanma, on_delete=models.CASCADE,null=True,blank=True)
    joylashtirish = models.ForeignKey(Joylashtirish, on_delete=models.CASCADE,null=True,blank=True)
    summa = models.PositiveSmallIntegerField()
    tolangan_summa = models.JSONField(default=list())
    tolandi = models.BooleanField(default=False)
    haqdor = models.BooleanField(default=False)
    sana = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.bemor.ism

class Xulosa(models.Model):
    matn = models.TextField()
    sana = models.DateField(null=True,blank=True)
    holat = models.CharField(max_length=50)
    tolov = models.ForeignKey(Tolov,on_delete=models.CASCADE)

    def __str__(self):
        return self.matn

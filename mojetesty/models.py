from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models import Sum
from django.db.models import F


# Create your models here.
class IpModels(models.Model):
    unique_ip_adress = models.TextField(max_length=100)
    
    def __str__(self):
        return self.unique_ip_adress


class MyTests(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    nazwa = models.CharField(max_length=255, null=True, blank=True)
    link1 = models.CharField(max_length=510)
    link2 = models.CharField(max_length=510)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, null=True, blank=True)
    test_views = models.IntegerField(default=0, null=True, blank=True)
    js_views = models.IntegerField(default=0, null=True, blank=True)
    button_like_clicked = models.ManyToManyField(User, related_name='mytest_button_like_clicked', blank=True)
    link_clicked = models.IntegerField(default=0, null=True, blank=True)
    unique_views = models.ManyToManyField(IpModels, related_name='mytest_unique_post_views', blank=True)
    sygnal_link1 = models.IntegerField(default=0)
    sygnal_link2 = models.IntegerField(default=0)
    sygnal_wynik = models.IntegerField(default=0)
    wyswietlenia_link1 = models.IntegerField(default=1)
    wyswietlenia_link2 = models.IntegerField(default=1)
    wyswietlenia_wynik = models.IntegerField(default=1)
    suma_wyswietlenia_linkow = models.IntegerField(default=1)
    ukonczenie_celu1 = models.IntegerField(default=0)
    ukonczenie_celu2 = models.IntegerField(default=0)
    suma_ukonczenia_celow = models.IntegerField(default=0)
    konwersja1 = models.FloatField(default=0,null=True, blank=True)
    konwersja2 = models.FloatField(default=0,null=True, blank=True)
    suma_konwersji = models.FloatField(default=0,)
    sygnal_konwersja1 = models.IntegerField(default=0)
    sygnal_konwersja2 = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.nazwa

    def total_likes(self):
        return self.button_like_clicked.count()


class KonwersjaDzienna(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    wersja = models.IntegerField(default=3)
    idtestu = models.ForeignKey(MyTests, null=True, on_delete=SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)
    datatestowa = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Użytkownik={self.user}; wersja={self.wersja}; idtestu={self.idtestu}; data={self.timestamp}"

    class Meta:
        verbose_name_plural = 'Dzienne konwersje'

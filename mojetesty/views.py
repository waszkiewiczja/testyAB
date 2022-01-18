from django.db.models.fields import FloatField
from mojetesty.models import KonwersjaDzienna, MyTests
from django.shortcuts import render

from users.views import loginPage
from .forms import MyTestForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import F
from django.db.models import Sum
from decimal import Decimal
from datetime import datetime, timedelta
from django.utils import timezone
import pytz
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def mojeTestyIndex(request):
    tests = MyTests.objects.all()
    context = {'tests':tests,}
    return render(request, 'mojetesty/mojetestyindex.html', context)


def utworzTest(request):
    form = MyTestForm()

    if request.method == 'POST':
        form = MyTestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            profile = request.user
            instance.user = profile
            instance.save()
            return redirect(reverse('mojetesty:szczegol', kwargs={'pk': instance.pk})  + '#code')


    context = {'form':form}
    return render(request, 'mojetesty/utworz.html', context)

@login_required(login_url='login')
def szczegolyTestu(request, pk):
    test = MyTests.objects.get(id=pk, user=request.user)
    Fview = MyTests.objects.filter(id=pk)
    Fview.update(test_views = F('test_views') +1)
    Fview.update(suma_wyswietlenia_linkow = (F('wyswietlenia_link1') + F('wyswietlenia_link2')))
    Fview.update(suma_ukonczenia_celow = (F('ukonczenie_celu1') + F('ukonczenie_celu2')))
    Fview.update(konwersja1 = (F('ukonczenie_celu1') * Decimal('100.0') / F('wyswietlenia_link1')))
    Fview.update(konwersja2 = (F('ukonczenie_celu2') * Decimal('100.0') / F('wyswietlenia_link2')))
    Fview.update(suma_konwersji = (F('suma_ukonczenia_celow') * Decimal('100.0') / F('suma_wyswietlenia_linkow')))
    

    data_konca= timezone.now()  
    roznica_dat = timedelta(days=3)
    data_poczatku = data_konca-roznica_dat

    zakres_dat = [data_poczatku.strftime("%Y-%m-%d %H:%M").split(" ")[0] + " " + (data_poczatku.strftime("%Y-%m-%d %H:%M").split(" ")[-1].replace(data_poczatku.strftime("%Y-%m-%d %H:%M").split(" ")[-1], '00:00')), data_konca.strftime("%Y-%m-%d %H:%M")]
    start, end = [datetime.fromisoformat(d) for d in zakres_dat]

    lista_pojedynczych_dni = [[start.date()+timedelta(d), start.date()+timedelta(d+1)] for d in range((end-start).days + 1)]
    lista_pojedynczych_dni[0][0], lista_pojedynczych_dni[-1][-1] = start, end

    lista_pojedynczych_dni = [(l[0].strftime('%Y-%m-%d %H:%M'), l[1].strftime('%Y-%m-%d %H:%M')) for l in lista_pojedynczych_dni]

    suma_konwersji = []
    data_konwersji = []
    suma_wersja1 = []
    suma_wersja2 = []


    for x in lista_pojedynczych_dni:
        print(x, "---", x[0].split(" ")[0], "***", x[1].split(" ")[0])
        #dane oryginalne:
        dziennakonwersja = KonwersjaDzienna.objects.filter(user=request.user, timestamp__gte=x[0].split(" ")[0], timestamp__lte=x[1].split(" ")[0])
        wynik_wersja1 = KonwersjaDzienna.objects.filter(wersja='1', timestamp__gte=x[0].split(" ")[0], timestamp__lte=x[1].split(" ")[0])
        wynik_wersja2 = KonwersjaDzienna.objects.filter(wersja='2', timestamp__gte=x[0].split(" ")[0], timestamp__lte=x[1].split(" ")[0])
        #dane testowe
        # dziennakonwersja = KonwersjaDzienna.objects.filter(user=request.user, datatestowa__gte=x[0].split(" ")[0], datatestowa__lte=x[1].split(" ")[0])
        # wynik_wersja1 = KonwersjaDzienna.objects.filter(wersja='1', datatestowa__gte=x[0].split(" ")[0], datatestowa__lte=x[1].split(" ")[0])
        # wynik_wersja2 = KonwersjaDzienna.objects.filter(wersja='2', datatestowa__gte=x[0].split(" ")[0], datatestowa__lte=x[1].split(" ")[0])
        suma_konwersji.append(dziennakonwersja.count())
        suma_wersja1.append(wynik_wersja1.count())
        suma_wersja2.append(wynik_wersja2.count())
        data_konwersji.append(x[0].split(" ")[0])
    
    lista_konwersji = list(zip(suma_konwersji[0:-1], data_konwersji[0:-1]))

    konw_roznica_dat = timedelta(days=1)
    
    dziennakonwersja = KonwersjaDzienna.objects.filter(user=request.user, timestamp__gte=data_konca.date(), timestamp__lte=data_konca.date()+konw_roznica_dat)
    # dziennakonwersja = KonwersjaDzienna.objects.filter(user=request.user, datatestowa__gte=data_konca.date(), datatestowa__lte=data_konca.date()+konw_roznica_dat)

    
    context = {'test':test, 'dziennakonwersja':dziennakonwersja, 'suma_konwersji':suma_konwersji[0:-1], 'data_konwersji':data_konwersji[0:-1], 'suma_wersja1':suma_wersja1[0:-1], 'suma_wersja2':suma_wersja2[0:-1]  } 
    return render(request, 'mojetesty/szczegol.html', context)


@login_required(login_url='login')
def aktualizujTest(request, pk):
    test = MyTests.objects.get(id=pk, user=request.user)
    form = MyTestForm(instance=test)

    if request.method == 'POST':
        form = MyTestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect(reverse('mojetesty:szczegol', kwargs={'pk': pk }) + '#code')

    context = {'form':form, 'test':test}
    return render(request, 'mojetesty/aktualizuj.html', context)


@login_required(login_url='login')
def usunTest(request, pk):
    test = MyTests.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        test.delete()
        messages.error(request, "Test został skasowany")
        return redirect('mojetesty:mojetestyindex')

    context = {'test':test}
    return render(request, 'mojetesty/usun.html', context)


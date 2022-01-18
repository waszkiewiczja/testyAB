from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MyTestsSerializer
from mojetesty.models import KonwersjaDzienna, MyTests
from mojetesty.api import serializers

from django.db.models import F


@api_view(['GET'])
def getRoutest(request):
    routes=[
        {'GET': '/api/tests'},
        {'GET': '/api/test/id'},
        {'POST': '/api/test/id/add/'},
    ]
    return Response(routes)


@api_view(['GET'])
def getTest(request,pk):
    test = MyTests.objects.get(id=pk)
    serializer = MyTestsSerializer(test, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addTest(request, pk):
    test = MyTests.objects.get(id=pk)
    data = request.data
    # ftest = MyTests.objects.filter(id=pk)
    # ftest.update(wyswietlenia_link2=F('wyswietlenia_link2') + 1)

    serializer = MyTestsSerializer(instance=test, data=request.data)
    print(data)
    if serializer.is_valid():
        print("jes to valid?")
        if 'sygnal_link1' in data:
            test.wyswietlenia_link1 = test.wyswietlenia_link1 + 1          
            print("dobrze sygnal link 1")
        elif 'sygnal_link2' in data:
            test.wyswietlenia_link2 = test.wyswietlenia_link2 + 1          
            print("dobrze 2 sygnal link 2")
        elif 'sygnal_wynik' in data:
            print('wynik')
            test.wyswietlenia_wynik = test.wyswietlenia_wynik + 1   
            
        if 'sygnal_konwersja1' in data:
            KonwersjaDzienna.objects.create(user=test.user, wersja='1', idtestu=test )
            test.ukonczenie_celu1 = test.ukonczenie_celu1 + 1
        elif 'sygnal_konwersja2' in data:
            print('konweresja dwa')
            KonwersjaDzienna.objects.create(user=test.user, wersja='2', idtestu=test )
            test.ukonczenie_celu2 = test.ukonczenie_celu2 + 1

        serializer.save()

    else:
        print("not valid")
    return Response(serializer.data)
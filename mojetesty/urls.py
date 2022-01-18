from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views
from django.views.generic import RedirectView

app_name = "mojetesty"
urlpatterns = [
    path("", views.mojeTestyIndex, name='mojetestyindex'),
    path("utworz/", views.utworzTest, name='create-new-test'),
    path("szczegol/<str:pk>/", views.szczegolyTestu, name='szczegol'),
    path("aktualizuj/<str:pk>/", views.aktualizujTest, name='aktualizuj'),
    path("usun/<str:pk>/", views.usunTest, name='usun'),
    path("api/", include('mojetesty.api.urls')),
]
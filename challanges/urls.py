
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('<int:id>/',views.monthly_chalanges_by_id ),
    path('<str:month>/',views.monthly_chalanges )

]

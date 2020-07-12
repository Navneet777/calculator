from django.urls import path
from .import views
urlpatterns = [
path('',views.index,name="index"),
path('lcm/',views.lcm,name="lcm"),
path('gcd/',views.gcd,name="gcd"),
]

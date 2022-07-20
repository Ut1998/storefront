from django.urls import path
from . import views

# URL config module
urlpatterns = [
    path('hello/', views.say_hello),
    path('bye/', views.say_Bye),
    path('home', views.home_page),
    path('add', views.add),
    path('', views.index)
]

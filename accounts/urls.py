from django.urls import path

from . import views

# URL config module
urlpatterns = [
    path('signup', views.signup, name="signup"),
]

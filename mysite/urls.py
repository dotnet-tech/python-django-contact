from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('home', views.Home, name="home"),
    path('contact', views.Contact, name="contact"),
    path('portfolio', views.Portfolio, name="portfolio")
]

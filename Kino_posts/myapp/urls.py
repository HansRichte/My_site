from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:film_id>/', views.film_detail, name='film_detail'),
]

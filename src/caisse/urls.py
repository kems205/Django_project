from django.urls import path
from . import views 

urlpatterns = [
     path('', views.acceuil, name='acceuil'),
    path('inscription/', views.register, name= 'inscription'),
    path('connexion/', views.logIn, name= 'connexion' ),
    path('deconnexion/', views.logOut, name="deconnexion"),
]

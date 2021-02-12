from django.urls import path
from . import views #se puede usar el .  o el nombre de la app

urlpatterns = [
    path('', views.index, name="inicio"),
    path('inicio/', views.index, name="index"),
    path('registro/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
]

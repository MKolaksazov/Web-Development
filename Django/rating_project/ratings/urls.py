from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_object/', views.add_object, name='add_object'),
    path('rate_object/<int:object_id>/', views.rate_object, name='rate_object'),
    path('average_rating/<int:object_id>/', views.average_rating, name='average_rating'),

    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    # Останалите URL маршрути
]

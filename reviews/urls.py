from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/',views.search,name='search'),
    path('Product/',views.product,name='Product'),
    path('login/',views.login,name='login'),
    path('Sign_up/',views.signup,name='register'),
]
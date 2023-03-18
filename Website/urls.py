from django.urls import path,include
import Website.views 
urlpatterns = [
    path('login/', Website.views.authentication.login, name='Login_Page'),
]

from django.urls import path,include
from account.views import UserRegistrationView,UserLoginView,UserProfileView,UserDetailsFormView
from rest_framework_simplejwt.views import TokenRefreshView,TokenBlacklistView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(),name='Register'),
    path('login/', UserLoginView.as_view(),name='Login'),
    path('profile/', UserProfileView.as_view(),name='Profile'),
    path('fill_details/', UserDetailsFormView.as_view(),name='User Details'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]

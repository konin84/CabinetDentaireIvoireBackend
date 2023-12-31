from django.urls import path
from . import views
# from .views import TestView
from .views import MyTokenObtainPairView, LogoutView


from rest_framework_simplejwt.views import (
    # MyTokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='token_verify'),

]

from django.urls import path,include
from .views import UserRegisterView,Login
urlpatterns = [
    
    path('signup/',UserRegisterView.as_view(),name = "signup"),
    path('signin/', Login.as_view(),name="signin")
]

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('Auth.urls')),
    path('api/company/',include('Company.urls')),
    path('api/employee/',include('Employee.urls')),
    path('api/device/',include('Phone.urls')),
    
    
]

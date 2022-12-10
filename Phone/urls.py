from django.urls import path
from .views import PhoneList,PhoneAllicationList
urlpatterns = [
    path('info/',PhoneList.as_view(), name="deviceinfo"),
    path('info/<int:id>/',PhoneList.as_view(), name="deviceinfo"),
    path('allocate/',PhoneAllicationList.as_view(), name="allocate"),
    path('allocate/<int:id>/',PhoneAllicationList.as_view(), name="allocateid")
]
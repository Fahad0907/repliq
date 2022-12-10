from django.db import models
from Auth.models import UserAccount
from Company.models import Companyinfo
# Create your models here.
device_type = [
    ('new','new'),
    ('used','used')
]
received_condition = [
    ('good','good'),
    ('bad','bad')
]
class Phone(models.Model):
    device_name = models.CharField(max_length=255,unique=True)
    device_condition = models.CharField(max_length=255,choices=device_type)
    is_booked = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.device_name
    
class PhoneAllocate(models.Model):
    device = models.ForeignKey(Phone,on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    company = models.ForeignKey(Companyinfo,on_delete=models.CASCADE)
    provide_time = models.DateField(auto_now_add=True)
    received_time = models.DateField(blank=True,null=True)
    received_condition = models.CharField(max_length=255,choices=received_condition)
    
    def __str__(self) -> str:
        return self.user.username + " " + self.device.device_name
from django.db import models
from Auth.models import UserAccount
# Create your models here.
class Companyinfo(models.Model):
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    company_name = models.CharField(unique=True,max_length=255)
    
    def __str__(self) -> str:
        return self.company_name

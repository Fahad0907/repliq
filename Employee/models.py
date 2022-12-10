from django.db import models
from Auth.models import UserAccount
from Company.models import Companyinfo

# Create your models here.
class EmployeeInfo(models.Model):
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    company = models.ForeignKey(Companyinfo,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.user.username) + " " + str(self.company.company_name)
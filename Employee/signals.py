from django.db.models.signals import post_save
from django.dispatch import receiver
from Auth.models import UserAccount
from Employee.models import EmployeeInfo
@receiver(post_save, sender= EmployeeInfo)
def post_save_make_employee(sender,instance,created, **kwargs):
    print(created)
    if created:
        user = UserAccount.objects.get(id = instance.user.id)
        user.isEmploye = True
        user.save()
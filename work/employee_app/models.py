from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()  
    # econtact = PhoneNumberField(blank=True)

    econtact = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)

    # If want to enter the no manually
    # eid = models.IntegerField()
    class Meta:
        db_table = "employee"





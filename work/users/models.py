from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "users"

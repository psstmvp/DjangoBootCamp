from django.db import models

# Create your models here.
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_contact=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

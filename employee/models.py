from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeSignup(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=50,null=True)
    father_name = models.CharField(max_length=50,null=True)
    mother_name = models.CharField(max_length=50,null=True)
    dob = models.DateField(null=True)
    adhar = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=200,null=True)
    bank_acc = models.CharField(max_length=50,null=True)
    blood_grp = models.CharField(max_length=20,null=True)
    pan = models.CharField(max_length=50,null=True)
    ifsc_code = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    img = models.FileField(null=True, default="account logo.png")

    def __str__(self):
        return self.user.username
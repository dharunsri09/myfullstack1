from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VacCenter(models.Model):
    cen_id=models.IntegerField()
    slot_coun=models.IntegerField()
    cen_name=models.CharField(max_length=200)
    cen_loc_city=models.TextField(null=True,blank=None)
    cen_loc_dis=models.CharField(max_length=200)
    dat_t=models.DateTimeField(auto_now=True)
    cre_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cen_name
    
    
class Booked(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    vac_name=models.CharField(max_length=100)
    center=models.ForeignKey(VacCenter,on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now=True)
    cre_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vac_name
    
class Bookings(models.Model):
    username=models.CharField(max_length=100)
    vaccine_center=models.CharField(max_length=100)
    e_mail=models.CharField(max_length=100,default="")
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=10)
    book_date=models.DateTimeField()
    is_verified=models.BooleanField(default=False)
    cre_time=models.DateTimeField(auto_now_add=True)

class MyModel(models.Model):
    image = models.ImageField(upload_to='static/img')
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user_name

    



    
    

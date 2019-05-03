from django.db import models
from django.contrib.auth.models import (AbstractUser,User)
from multiselectfield import MultiSelectField
# Create your models here.
class User(AbstractUser):
    is_tourist=models.BooleanField(default=False)
    is_guide=models.BooleanField(default=False)
    email = models.EmailField(unique=True)


class Tourist_Registration(models.Model):

    first_name=models.CharField(max_length=10,blank=False)
    last_name=models.CharField(max_length=10,blank=False)
    user_name=models.CharField(max_length=12,blank=False,unique=True)
    email_id=models.EmailField(max_length=255,blank=False)
    pass_word=models.CharField(max_length=20,blank=False)
    language=models.CharField(max_length=10,blank=False)
    gender=models.CharField(max_length=7,blank=False)
    phone_number = models.CharField(max_length=10, default="",blank=False,unique=True)
    age = models.CharField(max_length=2, blank=True)




class Guide_Registration(models.Model):

    first_name = models.CharField(max_length=10, blank=False)
    last_name=models.CharField(max_length=10,blank=False)
    user_name=models.CharField(max_length=12,blank=False,unique=True)
    email_id=models.EmailField(max_length=255,blank=False)
    pass_word=models.CharField(max_length=20,blank=False)
    gender= models.CharField(max_length=7,blank=True)
    native_place=models.CharField(max_length=25,blank=True)
    phone_number = models.CharField(max_length=10, default="", blank=False, unique=True)
    age = models.CharField(max_length=2, blank=False)
    Address=models.CharField(blank=False,max_length=50)


class language_Selection(models.Model):
    user=models.ForeignKey(Guide_Registration,on_delete=models.CASCADE)
    #user = models.CharField(max_length=25,null=True, blank=True, unique=True)
    languages_Know=(
                      ('Telugu','Telugu'),('Hindi','Hindi'),('English','English'),('Spanish','Spanish'),

                    )
    languages_select = MultiSelectField(choices=languages_Know,max_choices=4,max_length=100)



class Guide_Booking_Model(models.Model):
    tourist_username=models.ForeignKey(Tourist_Registration,on_delete=models.CASCADE,blank=True,null=True)
    guide_username=models.ForeignKey(Guide_Registration,on_delete=models.CASCADE)
    date_field=models.DateField(max_length=20)

    class Meta:
        unique_together = ('guide_username', 'date_field',)




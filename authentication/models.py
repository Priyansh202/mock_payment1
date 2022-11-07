from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    is_seller= models.BooleanField('Is seller', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
   # credits=models.CharField()


#class Balance(models.Model):
   #date = models.DateTimeField(default=timezone.now)
   # Keep the amount you start with
   #starting_balance = models.IntegerField()

   # Get the Sum of all expenses and do some simple subtraction
  # def get_current_balance(self):
       
    #   return self.starting_balance +added
    

#class Product(models.Model):
    #image = models.ImageField(null = False, blank = False) 
   # title = models.CharField(max_length=200, null = False, blank = False)
   # category = models.ForeignKey(Category, on_delete= models.CASCADE, default = '' , null = False)
   # author = models.CharField(blank= False, max_length= 100, null = True) 
   # description = models.TextField(max_length=200, null = False, blank = False) 
   # country = CountryField()is_active= models.BooleanField(default=False) 
    #created_at = models.DateField(default=datetime.now,blank=False, null = True)
class history(models.Model):
    qid = models.AutoField(primary_key=True)
    status= models.CharField(max_length=200, null = False, blank = False)
    update_time=models.DateTimeField(null=False, blank=False )
    transaction_id=models.CharField(max_length=200, null = False, blank = False)
    def __str__(self):
        return'{}'.format(self.status,self.update_time,self.transaction_id)

    


   
    
  
from django.db import models

# Create your models here.
class place_details(models.Model):
    place=models.CharField(max_length=10)
    number_of_beds=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20,default='null')



class user_details(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.CharField(max_length=100)
    Email=models.EmailField(max_length=50)
    Gender=models.CharField(max_length=10)
    Contact=models.CharField(max_length=12)
    Hometown = models.CharField(max_length=100, default='None')
    symptom1 = models.CharField(max_length=50,default='Null')
    symptom2 = models.CharField(max_length=50,default='Null')
    symptom3 = models.CharField(max_length=50,default='Null')
    symptom4 = models.CharField(max_length=50,default='Null')



class new_table(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.CharField(max_length=50, default='none')
    Email = models.EmailField(max_length=50)
    Gender = models.CharField(max_length=10)
    Contact = models.CharField(max_length=12)
    Hometown = models.CharField(max_length=100, default='None')
    symptom1 = models.CharField(max_length=50, default='Null')
    symptom2 = models.CharField(max_length=50, default='Null')
    symptom3 = models.CharField(max_length=50, default='Null')
    symptom4 = models.CharField(max_length=50, default='Null')
    status=models.CharField(max_length=10,default='NONE')
    place = models.CharField(max_length=10)
    number_of_beds = models.CharField(max_length=20)
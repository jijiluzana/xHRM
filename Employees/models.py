from django.db import models

from birthday import BirthdayField, BirthdayManager

# Create your models here.
class Employees(models.Model):

    CIVIL = (
        ('Single','Single'),
        ('Married','Married'),
    )
    Lastname=models.CharField(max_length=150)
    Firstname=models.CharField(max_length=150)
    Midname=models.CharField(max_length=150,null=True,blank=True)    
    Extname=models.CharField(max_length=150,null=True,blank=True)
    bday = BirthdayField()
    Civilstatus=models.CharField(max_length=25,choices=CIVIL)
    Contactnumber=models.CharField(max_length=150)
    Email=models.CharField(max_length=150,null=True,blank=True)
    Address=models.CharField(max_length=250,null=True,blank=True)
    
    def __str__(self):
        return f'{self.Lastname}, {self.Firstname}'




class Instructor(models.Model):

    CIVIL = (
        ('Single','Single'),
        ('Married','Married'),
    )
    Lastname=models.CharField(max_length=150)
    Firstname=models.CharField(max_length=150)
    Midname=models.CharField(max_length=150,null=True,blank=True)    
    Extname=models.CharField(max_length=150,null=True,blank=True)
    Civilstatus=models.CharField(max_length=25,choices=CIVIL)

    
    def __str__(self):
        return f'{self.Lastname}, {self.Firstname}'
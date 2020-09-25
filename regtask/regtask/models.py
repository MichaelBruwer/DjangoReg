from django.db import models

#Createing class to insert record into db
class RecordInsert(models.Model):
    #setting field to insert to as FName with a maxlenght of 100
    fname=models.CharField(max_length=100, blank=False, null=False)
    #setting field to insert to as LName with a maxlenght of 100
    lname=models.CharField(max_length=100, blank=False, null=False)
    #setting field to insert to as email with a maxlenght of 100
    email=models.CharField(max_length=100, blank=False, null=False, isEmail=True)
    #setting field to insert to as type with a maxlenght of 100
    Type=models.CharField(max_length=100, blank=False, null=False)
    #setting field to insert to as username with a maxlenght of 100
    username=models.CharField(max_length=100, unique=True, blank=False)
    #Setting field to insert to as password with minlenght of 8
    password=models.CharField(min_length=8, blank=False, null=False)
    

    class Meta:
        #Table in Db to send data to
        db_table="InsertTablenameHere"
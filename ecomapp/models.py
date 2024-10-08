from django.db import models

# Create your models here.
class product(models.Model): 
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,default="")
    subcatagory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField() 
    image=models.ImageField(upload_to="ecomapp/image",default="")
    
    def __str__(self):
        return self.product_name
    
class Contact(models.Model): 
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    add=models.CharField(max_length=50,default="")
    pin=models.CharField(max_length=6,default="")
    comm=models.CharField(max_length=500,default="") 
    
    
    def __str__(self):
        return self.name   
    
 
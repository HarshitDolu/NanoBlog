from django.db import models

# Create your models here.
class contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=300,blank=False)
    phone=models.CharField(max_length=11,blank=False)
    email=models.CharField(max_length=30,blank=True)

    content=models.TextField()
    timestamp=models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


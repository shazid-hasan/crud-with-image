from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    address=models.TextField(null=True)
    phone=models.IntegerField()
    image=models.ImageField(upload_to="media",null=True)

    def __str__(self):
        return self.name

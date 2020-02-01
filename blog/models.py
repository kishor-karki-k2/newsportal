from django.db import models

# Create your models here.
class Category(models.Model):
     title = models.CharField(max_length=20)

     def __str__(self):
          return self.title

class Blog(models.Model):
     title = models.CharField(max_length=100)
     description =models.TextField()
     image=models.ImageField(upload_to='news/')
     pub_date=models.DateField(auto_now=True)
     category=models.ForeignKey(Category,on_delete=models.CASCADE)

     def __str__(self):
          return self.title
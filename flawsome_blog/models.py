from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Blog(models.Model):
  id = models.BigAutoField(primary_key=True)
  Blog_name = models.CharField(max_length=1000)
  Blog_Date = models.DateField()
  Blog_Type = models.CharField( 
        max_length = 30, 
        default = 'Enter your Blog Category'
        ) 
  Author_Name = models.CharField(max_length=500)
  Cover_image = models.ImageField(upload_to ='uploads/blog')
  Blog_Description = models.TextField(max_length=30000)
  Blog_Short_Description = models.CharField(max_length=3000)

  def __str__(self): 
         return self.Blog_name
  



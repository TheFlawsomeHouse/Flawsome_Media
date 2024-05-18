from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

PROJECT_TYPE = ( 
    ("WEB DESIGN AND DEVELOPMENT", "WEB DESIGN AND DEVELOPMENT"), 
    ("BRANDING AND DESIGN IDENTITY", "BRANDING AND DESIGN IDENTITY"), 
    ("ADVERTISING AND MARKETING", "ADVERTISING AND MARKETING"), 
    ("CREATIVE CONSULTING", "CREATIVE CONSULTING"),  
    ("BRAND SHOOT", "BRAND SHOOT"),  
    ("SOCIAL MEDIA MARKETING", "SOCIAL MEDIA MARKETING"),  
) 
class Portfolio(models.Model):
  id = models.BigAutoField(primary_key=True)
  Project_name = models.CharField(max_length=1000)
  Project_Date = models.DateField()
  Project_Type = models.CharField( 
        max_length = 30, 
        choices = PROJECT_TYPE, 
        default = 'ADVERTISING AND MARKETING'
        ) 
  Client_Name = models.CharField(max_length=1000)
  Author_Name = models.CharField(max_length=500)
  Cover_image = models.FileField(upload_to ='uploads/video', null=True,
                                 validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv', 'jpg', 'PNG', 'jpeg', 'GIF'])])
  Image_1 = models.ImageField(upload_to ='uploads/')
  Image_2 = models.ImageField(upload_to ='uploads/')
  Image_3 = models.ImageField(upload_to ='uploads/')
  Image_4 = models.ImageField(upload_to ='uploads/')
  Image_5 = models.ImageField(upload_to ='uploads/')
  Image_6 = models.ImageField(upload_to ='uploads/')
  Image_7 = models.ImageField(upload_to ='uploads/')
  Image_8 = models.ImageField(upload_to ='uploads/')
  Project_Heading = models.CharField(max_length=1000)
  Project_Description = models.CharField(max_length=3000)

  def __str__(self): 
         return self.Project_name

SERVICE_TYPE = ( 
     ("NONE", "NONE"),
    ("WEB DESIGN AND DEVELOPMENT", "WEB DESIGN AND DEVELOPMENT"), 
    ("BRANDING AND DESIGN IDENTITY", "BRANDING AND DESIGN IDENTITY"), 
    ("ADVERTISING AND MARKETING", "ADVERTISING AND MARKETING"), 
    ("CREATIVE CONSULTING", "CREATIVE CONSULTING"),  
) 
class Contact(models.Model):
  id = models.BigAutoField(primary_key=True)
  Name = models.CharField(max_length=1000)
  Email = models.EmailField()
  Service_Type = models.CharField( 
        max_length = 30, 
      #   choices = SERVICE_TYPE,
      #   blank=False, 
      #   null=True
        ) 
  Mobile_Number = models.CharField(max_length=1000)
  Address = models.CharField(max_length=500)
  Budget = models.CharField(max_length=500)
  Project_Description = models.TextField(max_length=30000)

  def __str__(self): 
         return self.Name
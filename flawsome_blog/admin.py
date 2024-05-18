from django.contrib import admin
from flawsome_blog.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    #   list_display    = ['Project_name', 'Project_Date', 'Project_Type', 'Client_Name', 'Author_Name', 'Cover_image', 'Image_1', 'Image_2', 'Image_3', 'Image_4', 'Image_5', 'Image_6', 'Image_7', 'Image_8', 'Project_Heading', 'Project_Description']
    pass
      
admin.site.register(Blog, BlogAdmin)
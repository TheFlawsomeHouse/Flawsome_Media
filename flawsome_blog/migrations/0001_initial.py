# Generated by Django 5.0.2 on 2024-03-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Blog_name', models.CharField(max_length=1000)),
                ('Blog_Date', models.DateField()),
                ('Blog_Type', models.CharField(default='Enter your Blog Category', max_length=30)),
                ('Author_Name', models.CharField(max_length=500)),
                ('Cover_image', models.ImageField(upload_to='uploads/blog')),
                ('Blog_Description', models.TextField(max_length=30000)),
                ('Blog_Short_Description', models.TextField(max_length=3000)),

            ],
        ),
    ]

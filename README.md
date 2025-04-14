# Ex02 Django ORM Web Application
## Date: 14.04.2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin

from .models import Movies,MoviesAdmin

admin.site.register(Movies,MoviesAdmin)
 
models.py

from django.db import models
from django.contrib import admin

class Movies(models.Model):
    Userid  = models.IntegerField(primary_key=True)
    Username = models.CharField(max_length=30)
    Email_Id = models.CharField(max_length=30)
    Phone_number = models.IntegerField()
    Moviename =  models.CharField(max_length=20)
    Show_date = models.DateField()
    Show_time = models.TimeField()
    No_of_seats = models.IntegerField()


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('Userid','Username','Email_Id','Phone_number','Moviename','Show_date','Show_time','No_of_seats')
```



## OUTPUT
![alt text](<Screenshot 2025-04-14 132852.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully

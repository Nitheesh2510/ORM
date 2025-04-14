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

from django.db import models
from django import forms

class AddRouteModel(models.Model):
    def number():
        no = AddRouteModel.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    Route_id = models.IntegerField(unique=True,default=number)
    Bus_from=models.CharField(max_length=30)
    Bus_to=models.CharField(max_length=30)
    Journey_time=models.IntegerField()
    Price_per_seat=models.IntegerField()
    def __str__(self):
        return "Route Id "+str(self.Route_id)



class AddBusModel(models.Model):
    Bus_number=models.IntegerField()
    Route=models.ForeignKey(AddRouteModel, on_delete=models.CASCADE)
    Start_time=models.TimeField(auto_now=False, auto_now_add=False)
    Total_seats=models.IntegerField()

    def __str__(self):
        return "Bus Number "+str(self.Bus_number)

class Transactions(models.Model):
    User_name = models.CharField(max_length=200, null=True)
    Bus_details = models.ForeignKey(AddBusModel, on_delete=models.CASCADE)
    Passenger_name=models.CharField(max_length=200, null=True)
    No_of_passengers = models.IntegerField()
    Travel_date = models.DateField()

    def __str__(self):
        return "Transactions for "+str(self.User_name)


class AdduserModel(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Password=models.CharField(max_length=200)
    Gender = forms.ChoiceField(widget=forms.RadioSelect)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=10)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "User Name "+str(self.Name)

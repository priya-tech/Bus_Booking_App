from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import AdduserModel,AddRouteModel,AddBusModel,Transactions
from django.urls import reverse
from django.template.loader import render_to_string
from .forms import AdduserForm,AddRouteForm,AddBusForm
import datetime
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request, 'BusBooking/home.html')

def admincheck(request):
     if request.method == "POST":
         username = request.POST.get('username')
         password = request.POST.get('psw')
         if username == 'useradmin':
             if password == 'admin@123':
                 all_buses = AddBusModel.objects.all()
                 all_routes = AddRouteModel.objects.all()
                 return render(request, 'BusBooking/adminpage.html',{'all_buses':all_buses,'all_routes':all_routes})
             else:
                 return render(request, 'BusBooking/home.html', {'pass_error': True})
         else:
             return render(request, 'BusBooking/home.html', {'user_error': True})

def new_user(request):
    if request.method == "POST":
        form=AdduserForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('view_home'))
    else:
        form=AdduserForm()
        return render(request, 'BusBooking/newuser.html', {'form':form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('psw')
        checkname = AdduserModel.objects.filter(Name=username)
        if checkname:
            passwords=[x.Password for x in checkname]
            if password in passwords:
                 return render(request, 'BusBooking/usersdashboard.html',{'name':username})
            else:
                 return render(request, 'BusBooking/home.html', {'pass_error': True})
        else:
             return render(request, 'BusBooking/home.html', {'user_error': True})

def add_bus(request):
    all_routes=AddRouteModel.objects.all()
    all_buses=AddBusModel.objects.all()
    if request.method == "POST":
        s=AddBusModel()
        s.Bus_number = request.POST.get('bus_no')
        route = request.POST.get('route')
        s.Route = AddRouteModel.objects.get(Route_id=route)
        hours = int(request.POST.get('hours'))
        minutes = int(request.POST.get('minutes'))
        s.Start_time = datetime.time(hours,minutes)
        s.Total_seats = request.POST.get('total_seats')
        s.save()
        return render(request, 'BusBooking/adminpage.html',{'all_buses':all_buses,'all_routes':all_routes})
    else:
        return render(request, 'BusBooking/addbus.html', {'all_routes':all_routes, 'hours':range(0,24), 'minutes':range(0,61)})



def add_route(request):
    all_routes=AddRouteModel.objects.all()
    all_buses=AddBusModel.objects.all()
    if request.method == "POST":
        form=AddRouteForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'BusBooking/adminpage.html',{'all_buses':all_buses,'all_routes':all_routes})
    else:
        form=AddRouteForm()
        return render(request, 'BusBooking/addroute.html', {'form':form})

def update_bus(request,**kwargs):
    all_buses = AddBusModel.objects.all()
    all_routes = AddRouteModel.objects.all()
    if kwargs["action"] == 'edit':
        return render(request, "BusBooking/updatebus.html", {'all_buses':all_buses,'all_routes':all_routes})
    if kwargs["action"] == 'submit':
        bus_no = request.GET.get("bus_no")
        s = AddBusModel.objects.get(Bus_number=bus_no)
        new_route = request.GET.get("newroute")
        s.Route = AddRouteModel.objects.get(Route_id=new_route)
        hrs = int(request.GET.get("hours"))
        mins = int(request.GET.get("minutes"))
        s.Start_time = datetime.time(hrs,mins)
        s.Total_seats = request.GET.get("seats")
        s.save()
        return render(request, 'BusBooking/adminpage.html',{'all_buses':all_buses,'all_routes':all_routes})


def getUserInfo(request):
    if request.method == "GET" and request.is_ajax():
        Bus_num = request.GET.get("bus_no")
        try:
            bus_no = AddBusModel.objects.get(Bus_number = Bus_num)
        except:
            return JsonResponse({"success":False}, status=400)
        bus_info ={
        "Bus_no": bus_no.Bus_number,
        "Route_id": bus_no.Route.Route_id,
        "Bus_from": bus_no.Route.Bus_from,
        "Bus_to": bus_no.Route.Bus_to,
        "Journey_time": bus_no.Route.Journey_time,
        "Price_per_seat": bus_no.Route.Price_per_seat,
        "Total_seats":bus_no.Total_seats,
        "hrs":bus_no.Start_time.strftime("%H"),
        "mins":bus_no.Start_time.strftime("%M")
        }
        return JsonResponse({"bus_info":bus_info}, status=200)
    return JsonResponse({"success":False}, status=400)

def get_buses_info(request):
    if request.method == "GET" and request.is_ajax():
        get_bus_from = request.GET.get("busFrom")
        get_bus_to = request.GET.get("busTo")
        try:
            selected_buses=AddBusModel.objects.filter(Route__Bus_from=get_bus_from) and AddBusModel.objects.filter(Route__Bus_to=get_bus_to)
        except:
            return JsonResponse({"success":False}, status=400)

        data = []
        for buses in selected_buses:
            buses_info={
                "Bus_no": buses.Bus_number,
                "Route_id": buses.Route.Route_id,
                "Bus_from": buses.Route.Bus_from,
                "Bus_to": buses.Route.Bus_to,
                "Journey_time": buses.Route.Journey_time,
                "Price_per_seat": buses.Route.Price_per_seat,
                "Total_seats":buses.Total_seats,
                "hrs":buses.Start_time.strftime("%H"),
                "mins":buses.Start_time.strftime("%M")}
            data.append(buses_info)

        return JsonResponse({"buses_info":data}, status=200)
    return JsonResponse({"success":False}, status=400)


def delete_bus(request):
    all_routes=AddRouteModel.objects.all()
    all_buses=AddBusModel.objects.all()
    if request.method == "GET":
        bus_no = request.GET.get("bus_no")
        AddBusModel.objects.get(Bus_number=bus_no).delete()
        return render(request, 'BusBooking/adminpage.html',{'all_buses':all_buses,'all_routes':all_routes})

def delete_route(request):
    all_routes=AddRouteModel.objects.all()
    all_buses=AddBusModel.objects.all()
    if request.method == "GET":
        route_no = request.GET.get("route")
        AddRouteModel.objects.get(Route_id=route_no).delete()
        return render(request, 'BusBooking/adminpage.html',{'all_buses':all_buses,'all_routes':all_routes})

def bus_booking(request,name):
    all_buses = AddBusModel.objects.all()
    all_routes = AddRouteModel.objects.all()
    return render(request, 'BusBooking/booking.html', {'name':name,'all_buses':all_buses,'all_routes':all_routes})

def book_tickets(request,name):
    if request.method == "POST":
        passenger_name = request.POST.get("passenger_name")
        bus_no = request.POST.get("bus_no")
        bus_details = AddBusModel.objects.get(Bus_number=bus_no)
        date = request.POST.get("traveldate")
        seats = int(request.POST.get("seating"))
        s = Transactions()
        s.User_name = name
        s.Passenger_name = passenger_name
        s.Bus_details = bus_details
        s.Travel_date = date
        s.No_of_passengers = seats
        s.save()
        return render(request, 'BusBooking/home.html',{'thanks':True})

def booking_history(request,name):
    transactions = Transactions.objects.filter(User_name=name)
    return render(request, 'BusBooking/bookhistory.html', {'transactions':transactions})

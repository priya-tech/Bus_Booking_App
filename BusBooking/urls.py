from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='view_home'),
    path('admin_check', views.admincheck, name='admin_check'),
    path('new_user', views.new_user, name='new_user'),
    path('user_login', views.user_login, name='user_login'),
    path('add_bus', views.add_bus, name='add_bus'),
    path('add_route', views.add_route, name='add_route'),
    path('update_bus/<str:action>', views.update_bus, name='update_bus'),
    path('ajax/get_user_info', views.getUserInfo, name = 'get_user_info'),
    path('deletebus', views.delete_bus, name='delete_bus'),
    path('deleteroute', views.delete_route, name='delete_route'),
    path('booking/<str:name>', views.bus_booking, name='booking'),
    path('get_buses_info', views.get_buses_info, name='get_buses_info'),
    path('booktickets/<str:name>', views.book_tickets, name='book_tickets'),
    path('bookhistory/<str:name>', views.booking_history, name='booking_history'),
]

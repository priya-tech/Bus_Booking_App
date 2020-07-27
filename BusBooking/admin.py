from django.contrib import admin

# Register your models here.

from .models import Transactions,AddBusModel,AddRouteModel,AdduserModel
admin.site.register(Transactions)
admin.site.register(AddBusModel)
admin.site.register(AddRouteModel)
admin.site.register(AdduserModel)

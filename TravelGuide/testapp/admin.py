from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from testapp.models import Tourist_Registration,Guide_Registration ,User,language_Selection,Guide_Booking_Model
# Register your models here.
admin.site.register(Tourist_Registration)
admin.site.register(Guide_Registration)
admin.site.register(User,UserAdmin)
admin.site.register(language_Selection)
admin.site.register(Guide_Booking_Model)
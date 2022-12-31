from django.contrib import admin
from . models import Info

# Register your models here.
class InfoProfile(admin.ModelAdmin):
    list_display=('id','Full_Name','Phone_number','Email','Age','Blood_Group','Address','City','Pin_code','State','Last_donated')
admin.site.register(Info,InfoProfile)    

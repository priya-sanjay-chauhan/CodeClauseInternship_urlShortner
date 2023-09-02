from django.contrib import admin
from .models import Url
# Register your models here.
class dataDisplay(admin.ModelAdmin):
    list_display=('link','uuid')

admin.site.register(Url,dataDisplay)
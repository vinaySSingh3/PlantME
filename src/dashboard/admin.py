from django.contrib import admin
from .models import Feedback, showCal


@admin.register(showCal)
class showCalAdmin(admin.ModelAdmin):
     list_display = ['state_no', 'crop_name' ,'yieldd']

@admin.register(Feedback)
class feedbackAdmin(admin.ModelAdmin):
     list_display = [ 'name', 'email', 'subject']

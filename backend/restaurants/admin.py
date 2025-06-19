from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'rating')
    search_fields = ('name', 'address')
    list_filter = ('rating',)

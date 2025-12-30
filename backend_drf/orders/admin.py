from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['order', 'product', 'quantity', 'price', 'price', 'total_price']

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInLine]

admin.site.register(Order, OrderAdmin)

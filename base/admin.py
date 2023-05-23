from django.contrib import admin
from.models import*

'''
class ProductAdmin(admin.ModelAdmin):
    list_display = ("label", "price", "stock")

class CommandAdmin(admin.ModelAdmin):
    list_display = ("commandNumber", "name", "quality", "date_cmd")
'''
# Register your models here.
admin.site.register(Product)
admin.site.register(Command)
admin.site.register(CommandDetails)
admin.site.register(DeliveryInformation)
admin.site.register(Category)

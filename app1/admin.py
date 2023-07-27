from django.contrib import admin

from .models import *

@admin.register(Tolov)
class TolovAdmin(admin.ModelAdmin):
    list_display = ['bemor','summa','sana']
    search_fields = ['bemor','summa','sana']
    date_hierarchy = 'sana'
admin.site.register(Bemor)
admin.site.register(Yollanma)
admin.site.register(Xona)
admin.site.register(Joylashtirish)
# admin.site.register(Tolov)
admin.site.register(Xulosa)

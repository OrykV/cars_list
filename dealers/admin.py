from django.contrib import admin
from .models import Dealer

# Register your models here.

class DealerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_som', 'start_date')
    list_display_links = ('id', 'name',)
    list_filter = ('name',)
    list_editable = ('is_som',)
    search_fields = ('name', 'phone', 'email')
    list_per_page = 20

admin.site.register(Dealer, DealerAdmin)


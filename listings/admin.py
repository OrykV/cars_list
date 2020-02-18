from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published','make', 'model', 'year', 'odo', 'dealer', 'price')
    list_display_links = ('id','make', 'model')
    list_filter = ('make', 'model')
    list_editable = ('is_published',)
    search_fields = ('make', 'model', 'year', 'odo', 'dealer', 'price')
    list_per_page = 20


admin.site.register(Listing, ListingAdmin)
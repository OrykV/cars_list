from django.urls import path

from . import views

urlpatterns = [
    path('list', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('add_new', views.add_new, name='add_new')
]
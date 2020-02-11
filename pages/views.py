from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import type_choices, engine_choices, color_choices, price_choices

from listings.models import Listing
from dealers.models import Dealer


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'type_choices': type_choices,
        'engine_choices': engine_choices,
        'color_choices': color_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    dealers = Dealer.objects.order_by('-start_date')[1:4]

    som_dealers = Dealer.objects.all().filter(is_som=True)

    context = {
        'dealers': dealers,
        'som_dealers': som_dealers
    }
    return render(request, 'pages/about.html', context)

from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import type_choices, engine_choices, color_choices, price_choices

from .models import Listing
from dealers.models import Dealer


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Type
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            queryset_list = queryset_list.filter(type__iexact=type)

    # Engine
    if 'engine' in request.GET:
        engine = request.GET['engine']
        if engine:
            queryset_list = queryset_list.filter(engine_type__iexact=engine)

    # Color
    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            queryset_list = queryset_list.filter(color__iexact=color)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price == '100000':
            queryset_list = queryset_list.filter(price__gte=price)
        else:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'type_choices': type_choices,
        'engine_choices': engine_choices,
        'color_choices': color_choices,
        'price_choices': price_choices,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)


def add_new(request):
    queryset_list = Dealer.objects
    print(queryset_list)
    context = {
        'type_choices': type_choices,
        'engine_choices': engine_choices
    }
    return render(request, 'listings/add_new.html', context)

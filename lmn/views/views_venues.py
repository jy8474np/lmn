from django.shortcuts import render, redirect, get_object_or_404

from ..models import Venue, Artist, Note, Show
from ..forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator


def venue_list(request):
    form = VenueSearchForm()
    search_name = request.GET.get('search_name')

    if search_name:
        #search for this venue, display results
        venues = Venue.objects.filter(name__icontains=search_name).order_by('name')
        paginator = Paginator(venues,5)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            venues = paginator.page(page)
        except:
            venues = paginator.page(paginator.num_pages)
    else :
        venues = Venue.objects.all().order_by('name')   # Todo paginate
        paginator = Paginator(venues,5)

        #it will default grab page 1
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            venues = paginator.page(page)
        except:
            venues = paginator.page(paginator.num_pages)

    return render(request, 'lmn/venues/venue_list.html', { 'venues': venues, 'form': form, 'search_term': search_name })


def artists_at_venue(request, venue_pk):   # pk = venue_pk
    """ Get all of the artists who have played a show at the venue with pk provided """

    shows = Show.objects.filter(venue=venue_pk).order_by('-show_date') 
    venue = Venue.objects.get(pk=venue_pk)

    return render(request, 'lmn/artists/artist_list_for_venue.html', { 'venue': venue, 'shows': shows })


def venue_detail(request, venue_pk):
    venue = get_object_or_404(Venue, pk=venue_pk)
    return render(request, 'lmn/venues/venue_detail.html' , { 'venue': venue })

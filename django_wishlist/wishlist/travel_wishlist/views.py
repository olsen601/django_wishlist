from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, ReviewPlaceForm


def place_list(request):
#route for wishlist.html
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')


    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


def places_visited(request):
#route for visited.html
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

def place_is_visited(request):
#route to mark object as visited then display the wishlist.html page
    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')

def place(request, pk):
#route for the place.html page
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
    #save notes and dates from form
        form = ReviewPlaceForm(request.POST, request.FILES, instance=place)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place', pk=pk)

    else:
        rp_form = ReviewPlaceForm(instance=place)
        return render(request, 'travel_wishlist/place.html', {'place': place, 'rp_form': rp_form})

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from places.models import Place, Image
def get_geojson(request):
    places = Place.objects.all()
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        features = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.coordinate_lng, place.coordinate_lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place', args=(place.id, )),

            }
        }
        geojson['features'].append(features)
    places_geojson = {
        'places': geojson
    }
    return render(request, "index.html", context=places_geojson)


def get_place(request, place_id):
    imges = []
    place = get_object_or_404(Place, pk=place_id)
    for image in place.images.all():
        imges.append(image.image.url)
    place_context = {
        "title": place.title,
        "imgs": imges,
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": place.coordinate_lng,
            "lat": place.coordinate_lat
        }
    }

    return JsonResponse(place_context, json_dumps_params={'ensure_ascii': False, 'indent': 2})
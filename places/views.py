from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


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
    place = Place.objects.prefetch_related('images').get(pk=place_id)
    images = [image.image.url for image in place.images.all()]
    place_context = {
        "title": place.title,
        "imgs": images,
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": place.coordinate_lng,
            "lat": place.coordinate_lat
        }
    }

    return JsonResponse(
        place_context,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )

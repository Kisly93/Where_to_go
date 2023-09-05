import requests
from urllib.parse import urlparse
from pathlib import Path
from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Добавить место на карту'


    def add_arguments(self, parser):
        parser.add_argument('place', type=str, help='Введите путь к файлу с данными')

    def handle(self, *args, **kwargs):
        place_url = kwargs['place']
        response = requests.get(place_url)
        response.raise_for_status()

        place_payload = response.json()

        place_obj, created = Place.objects.get_or_create(
            title=place_payload['title'],
            coordinate_lng=float(place_payload['coordinates']['lng'].replace(',', '.')),
            coordinate_lat=float(place_payload['coordinates']['lat'].replace(',', '.')),
            defaults={
                'short_description': place_payload.get('short_description', ''),
                'long_description': place_payload.get('long_description', ''),
            }
        )
        if not created:
            return
        for image_url in place_payload.get('imgs', []):
            self.download_img(image_url, place_obj)

    def download_img(self, image_url, place_obj):
        response = requests.get(image_url)
        response.raise_for_status()

        filename = Path(urlparse(image_url).path).name
        Image.objects.create(
            location=place_obj,
            image=ContentFile(response.content, name=filename)
        )





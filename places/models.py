from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    short_description = models.TextField(verbose_name='Короткое описание',
                                         blank=True
                                         )
    long_description = HTMLField(verbose_name='Длинное описание', blank=True)
    coordinate_lng = models.FloatField(verbose_name='Долгота')
    coordinate_lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(Place, on_delete=models.CASCADE,
                                 verbose_name='Локация', related_name='images'
                                 )
    image = models.ImageField(verbose_name='Картинка', upload_to='media/')
    order = models.PositiveIntegerField(verbose_name='Порядок',
                                        default=0, db_index=True
                                        )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.location.title

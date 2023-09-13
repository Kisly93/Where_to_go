from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ('image_preview',)
    extra = 3

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; max-width: auto;" />',
                           obj.image.url
                           )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        ImageInline, ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('location', 'image')
    list_filter = ('location',)
    raw_id_fields = ('location',)
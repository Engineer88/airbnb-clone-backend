from django.contrib import admin
from .models import Experiences, Perk


# Register your models here.
@admin.register(Experiences)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "start",
        "end",
        "created_at",
    )

    list_filter = ("category",)


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "detail",
        "explanation",
    )

from django.contrib import admin
from .models import Event

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'time', 'event_id', 'venue', 'image', 'address', 'city', 'state')
    list_filter = ("date", "time")
    list_display = ("event_id", "name", "venue", "date")

admin.site.register(Event, ReviewAdmin)

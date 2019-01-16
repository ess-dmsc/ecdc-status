from django.contrib import admin

from django.utils import timezone
from .models import EventIcon, Event
from django.utils.translation import gettext_lazy as _

class FilterOld(admin.SimpleListFilter):
    title = _('future events')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'show'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('false', _('Show old')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'false':
            return queryset.filter()
        CurrentlyOngoing = queryset.exclude(EndDate__isnull = True).filter(EndDate__gte = timezone.now()).filter(StartDate__lt = timezone.now())
        return queryset.filter(StartDate__gte=timezone.now()).union(CurrentlyOngoing)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('Title', 'StartDate', 'Icon', 'isOngoing')
    list_filter = (FilterOld, )
    
admin.site.register(EventIcon)

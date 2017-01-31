from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'product', 'user', )

    list_display = ('created_at', 'product', 'user', 'used')

    search_fields = ['user']


admin.site.register(Ticket, TicketAdmin)

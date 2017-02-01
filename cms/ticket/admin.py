from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'product', 'user', )

    list_display = ('created_at', 'product', 'user', 'used')

    search_fields = ['user__first_name', 'user__last_name']

    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False


admin.site.register(Ticket, TicketAdmin)

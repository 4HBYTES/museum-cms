from django.contrib import admin
from .models import FrontUser


class FrontUserAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'email', 'password',)

    list_display = ('email', 'first_name', 'last_name',)

    def has_add_permission(self, request):
        return False


admin.site.register(FrontUser, FrontUserAdmin)

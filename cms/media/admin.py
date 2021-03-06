from django.contrib import admin
from .models import Article, Event


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at',)

    list_display = ('name', 'created_at',)

    search_fields = ['name']


admin.site.register(Article, ArticleAdmin)


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

    list_display = ('name', 'place', 'date',)

    search_fields = ['name']


admin.site.register(Event, EventAdmin)

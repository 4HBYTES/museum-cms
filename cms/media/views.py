from django.http import HttpResponse
from django.views.generic import View
from .models import Article, Event
import json


class NewsView(View):

    def get(self, request):
        all_articles = []
        articles = Article.objects.all()
        for article in articles:
            all_articles.append(article.to_view())

        json_articles = json.dumps(all_articles)
        return HttpResponse(json_articles, content_type='application/json')


class EventsView(View):

    def get(self, request):
        all_events = []
        events = Event.objects.all()
        for event in events:
            all_events.append(event.to_view())

        json_events = json.dumps(all_events)
        return HttpResponse(json_events, content_type='application/json')

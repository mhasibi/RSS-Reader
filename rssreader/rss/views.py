from django.http import HttpResponse
import feedparser

def index(request):
    url = 'https://www.djangoproject.com/rss/weblog/'

    feed = feedparser.parse(url)

    return HttpResponse(feed["feed"]["title"])


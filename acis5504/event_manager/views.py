import datetime

from event_manager.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def index(request):
    recent_events = Event.objects.all().order_by('date') [:5]	
    now = datetime.datetime.now()
    t = get_template('index.html')
    html = t.render(Context({'recent_events': recent_events}))
    return HttpResponse(html)

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    registrations = Registration.objects.filter(event__in=(event_id))
    players = Player.objects.filter(player_id__in(registrations.player))
    t = get_template('event.html')
    html = t.render(Context({'event': event, 'players': players}))
    return HttpResponse(html)	


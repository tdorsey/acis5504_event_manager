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
    players = []
    matches_in_round = set()
    match_dict = dict()
    event = get_object_or_404(Event, pk=event_id)
    registration = Registration.objects.filter(event__in=(event_id))
    current_registrations = registration.prefetch_related('player')
    matches = Match.objects.filter(event__in=(event_id))
    current_round = 1
    while current_round <= event.rounds:
        current_matches =  matches.filter(round=current_round)
        for match in current_matches:
            matches_in_round.add(match)
        match_dict[current_round] = matches_in_round
        current_round += 1
    for reg in current_registrations:
        players.append(reg.player)
    #hardcode a winner for now
    winner = players[1]
    t = get_template('event.html')
    c = Context()
    c['event'] = event
    c['players'] = players
    c['matches'] = match_dict	
    c['winner'] = winner
    html = t.render(c)
    return HttpResponse(html)	


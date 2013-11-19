from django.contrib import admin
from event_manager.models import Event
from event_manager.models import Person
from event_manager.models import Player
from event_manager.models import Judge
from event_manager.models import Match
from event_manager.models import Registration
from event_manager.models import Standing
from event_manager.models import Event_Level

admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Player)
admin.site.register(Judge)
admin.site.register(Match)
admin.site.register(Registration)
admin.site.register(Standing)
admin.site.register(Event_Level)

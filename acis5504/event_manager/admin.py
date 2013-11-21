from django.contrib import admin
from event_manager.models import *

admin.site.register(Event, EventAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Standing, StandingAdmin)
admin.site.register(Event_Level, Event_Level_Admin)
admin.site.register(Pro_Level, Pro_Level_Admin)

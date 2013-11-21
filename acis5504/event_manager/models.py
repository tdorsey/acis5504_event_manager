# Create your models here.
from django.db import models
from django.contrib import admin


class Person(models.Model):
	def __unicode__(self):
		return str(self.pk)
	person_id = models.AutoField('Person ID', primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	dob = models.DateField('Date of Birth')
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	region = models.CharField(max_length=200)
	postal_code = models.CharField(max_length=5) 
	country = models.CharField(max_length=2)
	banned_until = models.DateField('Banned Until', blank=True, null=True)
	active_since = models.DateField('Join Date')
	class Meta:
		abstract = True 

class Pro_Level(models.Model):
	def __unicode__(self):
       		return str(self.pk)  
	level = models.AutoField('Pro Level', primary_key=True)
	description = models.CharField(max_length=500)
	class Meta:
		verbose_name_plural = "Pro Levels"
class Pro_Level_Admin(admin.ModelAdmin):
	list_display = ('level', 'description')

class Player(Person):
	def __unicode__(self):
		return "{0}, {1} - {2}".format(self.last_name, self.first_name, self.person_id)  
	rank = models.PositiveIntegerField(blank=True, null=True)
	points = models.PositiveIntegerField(default=0)
	lifetime_points = models.PositiveIntegerField(default=0)
	pro_level = models.ForeignKey(Pro_Level, blank=True, null=True)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('person_id', 'last_name', 'first_name')

#Judges explicitly are not people, because then it is not possible to make an existing player a judge without reintering basic info	
class Judge(models.Model):
	def __unicode__(self):
		p = self.player
		return "{0}, {1} - {2}".format(p.last_name, p.first_name, self.level)  
	def Judge(self):
		p = self.player	
		return "{0}, {1} - {2}".format(p.last_name, p.first_name, p.person_id)  
		return self.level
	player = models.OneToOneField(Player)
	level = models.PositiveIntegerField()
	certified_until = models.DateField('Certified Until')

class JudgeAdmin(admin.ModelAdmin):
    list_display = ('Judge', 'level')


class Event_Level(models.Model):
	def __unicode__(self):
		return str(self.pk)  
	level = models.IntegerField('Rules Enforcement Level', primary_key=True)
	description = models.CharField(max_length=200)
	points_multiplier = models.PositiveIntegerField()
	required_judge_level = models.PositiveIntegerField()
	class Meta:
        	verbose_name_plural = "Event Levels"

class Event_Level_Admin(admin.ModelAdmin):
    list_display = ('level', 'description')

class Event(models.Model):
	def __unicode__(self):
		return "{0} - {1}".format(self.date, self.description) 
	event_id = models.AutoField('Event ID', primary_key=True)
	description = models.CharField(max_length=500)
	date = models.DateField()
	location = models.CharField(max_length=200)
	level = models.ForeignKey(Event_Level)
	rounds = models.IntegerField()
	format = models.CharField(max_length=50)
	head_judge = models.ForeignKey(Judge, related_name='head_judge')
	judges = models.ManyToManyField(Judge, related_name='floor_judge', blank=True, null=True)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'date','description')

class Registration(models.Model):
	def __unicode__(self):
		return str(self.pk)  
	event = models.ForeignKey(Event)
	player = models.ForeignKey(Player)
	dropped = models.NullBooleanField(blank=True, null=True)
	dropped_round = models.IntegerField(blank=True, null=True)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'player')

class Match(models.Model):
	def __unicode__(self):
		return str(self.pk)  
	match_id = models.AutoField('Match ID', primary_key=True)
	event = models.ForeignKey(Event)
	round = models.IntegerField()	
	player1 = models.ForeignKey(Player, related_name='player_1')
	player2 = models.ForeignKey(Player, related_name='player_2')
	games = models.IntegerField()	
	result = models.IntegerField('Match Result')
	class Meta:
        	verbose_name_plural = "Matches"	

class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'event', 'round', 'player1', 'player2')

class Standing(models.Model):
	def __unicode__(self):
		return str(self.pk)  
	player = models.ForeignKey(Player)
	event = models.ForeignKey(Event)
	ranking = models.IntegerField()
	points = models.IntegerField()
	opponent_match_win = models.IntegerField()
	game_win = models.IntegerField()
	opponent_game_win = models.IntegerField()

class StandingAdmin(admin.ModelAdmin):
    list_display = ('player', 'ranking', 'event')

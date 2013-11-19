# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Registration.dropped_round'
        db.alter_column('event_manager_registration', 'dropped_round', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Registration.dropped'
        db.alter_column('event_manager_registration', 'dropped', self.gf('django.db.models.fields.NullBooleanField')(null=True))

    def backwards(self, orm):

        # Changing field 'Registration.dropped_round'
        db.alter_column('event_manager_registration', 'dropped_round', self.gf('django.db.models.fields.IntegerField')(default='null'))

        # Changing field 'Registration.dropped'
        db.alter_column('event_manager_registration', 'dropped', self.gf('django.db.models.fields.BooleanField')())

    models = {
        'event_manager.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'event_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'head_judge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'head_judge'", 'to': "orm['event_manager.Judge']"}),
            'judges': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'floor_judge'", 'to': "orm['event_manager.Judge']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Event_Level']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rounds': ('django.db.models.fields.IntegerField', [], {})
        },
        'event_manager.event_level': {
            'Meta': {'object_name': 'Event_Level'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'level': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'points_multiplier': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'required_judge_level': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'event_manager.judge': {
            'Meta': {'object_name': 'Judge', '_ormbases': ['event_manager.Person']},
            'certified_until': ('django.db.models.fields.DateField', [], {}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['event_manager.Person']", 'primary_key': 'True'})
        },
        'event_manager.match': {
            'Meta': {'object_name': 'Match'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Event']"}),
            'games': ('django.db.models.fields.IntegerField', [], {}),
            'match_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_1'", 'to': "orm['event_manager.Player']"}),
            'player2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_2'", 'to': "orm['event_manager.Player']"}),
            'result': ('django.db.models.fields.IntegerField', [], {}),
            'round': ('django.db.models.fields.IntegerField', [], {})
        },
        'event_manager.person': {
            'Meta': {'object_name': 'Person'},
            'active_since': ('django.db.models.fields.DateField', [], {}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'banned_until': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'player_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'event_manager.player': {
            'Meta': {'object_name': 'Player', '_ormbases': ['event_manager.Person']},
            'lifetime_points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['event_manager.Person']", 'primary_key': 'True'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'pro_level': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['event_manager.Pro_Level']"}),
            'rank': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'event_manager.pro_level': {
            'Meta': {'object_name': 'Pro_Level'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'level': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'event_manager.registration': {
            'Meta': {'object_name': 'Registration'},
            'dropped': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'dropped_round': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Player']"})
        },
        'event_manager.standing': {
            'Meta': {'object_name': 'Standing'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Event']"}),
            'game_win': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opponent_game_win': ('django.db.models.fields.IntegerField', [], {}),
            'opponent_match_win': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Player']"}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'ranking': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['event_manager']
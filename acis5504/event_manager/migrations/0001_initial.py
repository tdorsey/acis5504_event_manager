# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('event_manager_person', (
            ('player_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('banned_until', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('active_since', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('event_manager', ['Person'])

        # Adding model 'Judge'
        db.create_table('event_manager_judge', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['event_manager.Person'], primary_key=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('certified_until', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('event_manager', ['Judge'])

        # Adding model 'Pro_Level'
        db.create_table('event_manager_pro_level', (
            ('level', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('event_manager', ['Pro_Level'])

        # Adding model 'Player'
        db.create_table('event_manager_player', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['event_manager.Person'], primary_key=True)),
            ('rank', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('lifetime_points', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('pro_level', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['event_manager.Pro_Level'], blank=True)),
        ))
        db.send_create_signal('event_manager', ['Player'])

        # Adding model 'Event_Level'
        db.create_table('event_manager_event_level', (
            ('level', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('points_multiplier', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('required_judge_level', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('event_manager', ['Event_Level'])

        # Adding model 'Event'
        db.create_table('event_manager_event', (
            ('event_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Event_Level'])),
            ('rounds', self.gf('django.db.models.fields.IntegerField')()),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('head_judge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Judge'], related_name='head_judge')),
        ))
        db.send_create_signal('event_manager', ['Event'])

        # Adding M2M table for field judges on 'Event'
        m2m_table_name = db.shorten_name('event_manager_event_judges')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['event_manager.event'], null=False)),
            ('judge', models.ForeignKey(orm['event_manager.judge'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'judge_id'])

        # Adding model 'Registration'
        db.create_table('event_manager_registration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Event'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Player'])),
            ('dropped', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dropped_round', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('event_manager', ['Registration'])

        # Adding model 'Match'
        db.create_table('event_manager_match', (
            ('match_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Event'])),
            ('round', self.gf('django.db.models.fields.IntegerField')()),
            ('player1', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Player'], related_name='player_1')),
            ('player2', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Player'], related_name='player_2')),
            ('games', self.gf('django.db.models.fields.IntegerField')()),
            ('result', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('event_manager', ['Match'])

        # Adding model 'Standing'
        db.create_table('event_manager_standing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Player'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event_manager.Event'])),
            ('ranking', self.gf('django.db.models.fields.IntegerField')()),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
            ('opponent_match_win', self.gf('django.db.models.fields.IntegerField')()),
            ('game_win', self.gf('django.db.models.fields.IntegerField')()),
            ('opponent_game_win', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('event_manager', ['Standing'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('event_manager_person')

        # Deleting model 'Judge'
        db.delete_table('event_manager_judge')

        # Deleting model 'Pro_Level'
        db.delete_table('event_manager_pro_level')

        # Deleting model 'Player'
        db.delete_table('event_manager_player')

        # Deleting model 'Event_Level'
        db.delete_table('event_manager_event_level')

        # Deleting model 'Event'
        db.delete_table('event_manager_event')

        # Removing M2M table for field judges on 'Event'
        db.delete_table(db.shorten_name('event_manager_event_judges'))

        # Deleting model 'Registration'
        db.delete_table('event_manager_registration')

        # Deleting model 'Match'
        db.delete_table('event_manager_match')

        # Deleting model 'Standing'
        db.delete_table('event_manager_standing')


    models = {
        'event_manager.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'event_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'head_judge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Judge']", 'related_name': "'head_judge'"}),
            'judges': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'blank': 'True', 'to': "orm['event_manager.Judge']", 'related_name': "'floor_judge'"}),
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
            'player1': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Player']", 'related_name': "'player_1'"}),
            'player2': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['event_manager.Player']", 'related_name': "'player_2'"}),
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
            'pro_level': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['event_manager.Pro_Level']", 'blank': 'True'}),
            'rank': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'event_manager.pro_level': {
            'Meta': {'object_name': 'Pro_Level'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'level': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'event_manager.registration': {
            'Meta': {'object_name': 'Registration'},
            'dropped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dropped_round': ('django.db.models.fields.IntegerField', [], {}),
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
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Producto'
        db.create_table(u'productos_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Titulo', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('Descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('Precio', self.gf('django.db.models.fields.DecimalField')(default=29.99, max_digits=100, decimal_places=2)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'productos', ['Producto'])


    def backwards(self, orm):
        # Deleting model 'Producto'
        db.delete_table(u'productos_producto')


    models = {
        u'productos.producto': {
            'Descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Producto'},
            'Precio': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '100', 'decimal_places': '2'}),
            'Titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['productos']
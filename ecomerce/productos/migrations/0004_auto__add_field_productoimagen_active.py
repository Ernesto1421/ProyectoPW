# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProductoImagen.active'
        db.add_column(u'productos_productoimagen', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProductoImagen.active'
        db.delete_column(u'productos_productoimagen', 'active')


    models = {
        u'productos.producto': {
            'Descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Producto'},
            'Precio': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '100', 'decimal_places': '2'}),
            'Precio_Ventas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            'Titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'productos.productoimagen': {
            'Meta': {'object_name': 'ProductoImagen'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Producto']"}),
            'thumbail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['productos']
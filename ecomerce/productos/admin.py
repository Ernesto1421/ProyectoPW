from django.contrib import admin

from .models import Producto, ProductoImagen
class ProductAdmin(admin.ModelAdmin):
    date_hchuy = 'timestamp'
    serch_fields = ['Titulo', 'Descripcion']
    list_display = ['__unicode__', 'Titulo','Precio','active','updated']
    list_editable = ['Precio', 'active']
    list_filter = ['Precio', 'active' ]
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("Titulo",)}
    class Meta:
        model = Producto
admin.site.register(Producto, ProductAdmin)
admin.site.register(ProductoImagen)
# Register your models here.

from django.db import models

# Create your models here.
class Producto(models.Model):
    Titulo = models.CharField(max_length=120)
    Descripcion = models.TextField(null=True, blank=True)
    Precio = models.DecimalField(decimal_places=2, max_digits=100, default= 29.99)
    Precio_Ventas = models.DecimalField(decimal_places=2, max_digits=100, null= True, blank= True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.Titulo
    
    def get_price(self):
        return self.Precio

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto)
    imagen = models.ImageField(upload_to='productos/imagenes/')
    featured = models.BooleanField(default = False)
    thumbail = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now_add= False, auto_now= True)
    active = models.BooleanField(default=True)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.producto.Titulo
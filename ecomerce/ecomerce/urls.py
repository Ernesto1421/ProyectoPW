from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'productos.views.home', name='home'),
    url(r'^productos/$', 'productos.views.todos', name='productos'),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView, DetailView, ListView

from django.contrib import admin
admin.autodiscover()

from fiberdb.models import *
from fiberdb.forms import *

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(
            template_name='fiberdb/base.html')),
    url(r'^buildings/',
        ListView.as_view(
            queryset=Building.objects,
            context_object_name='building_list',
            template_name='fiberdb/buildings.html')),
    # Examples:
    # url(r'^$', 'fiber.views.home', name='home'),
    # url(r'^fiber/', include('fiber.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

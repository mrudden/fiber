from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib import admin
admin.autodiscover()
from fiberdb.models import *
from fiberdb.forms import *

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(
            template_name='fiberdb/base.html')),
    # Buildings
    url(r'^buildings/$',
        ListView.as_view(
            queryset=Building.objects.order_by('building_name'),
            context_object_name='building_list',
            template_name='fiberdb/buildings.html')),
    url(r'^buildings/add/$',
        CreateView.as_view(
            form_class=AddBuilding,
            model='Building',
            success_url='/buildings/',
            template_name='fiberdb/add_building.html')),
    # LAN Rooms
    url(r'^lanrooms/$',
        ListView.as_view(
            queryset=LanRoom.objects.order_by('building_id'),
            context_object_name='lanroom_list',
            template_name='fiberdb/lanrooms.html')),
    url(r'^lanrooms/add/$',
        CreateView.as_view(
            form_class=AddLanRoom,
            model='LanRoom',
            success_url='/lanrooms/',
            template_name='fiberdb/add_lanroom.html')),
    # Racks
    url(r'^racks/$',
        ListView.as_view(
            queryset=Rack.objects.order_by('rack_name'),
            context_object_name="rack_list",
            template_name='fiberdb/racks.html')),
    url(r'^racks/add/$',
        CreateView.as_view(
            form_class=AddRack,
            model='Rack',
            success_url='/racks/',
            template_name='fiberdb/add_rack.html')),
    
    # Admin stuff
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

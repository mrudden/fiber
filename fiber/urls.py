from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from fiberdb.models import *
from fiberdb.forms import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(
            template_name='fiberdb/base.html')),
    # Buildings
    url(r'^buildings/$',
        ListView.as_view(
            queryset=Building.objects,
            context_object_name='building_list',
            template_name='fiberdb/buildings.html')),
    url(r'^buildings/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Building,
            template_name='fiberdb/buildings_detail.html')),
#    url(r'^buildings/add/$',
#        CreateView.as_view(
#            form_class=AddBuilding,
#            model='Building',
#            success_url='/buildings/',
#            template_name='fiberdb/buildings_add.html')),
    # LAN Rooms
    url(r'^lanrooms/$',
        ListView.as_view(
            queryset=LanRoom.objects,
            context_object_name='lanroom_list',
            template_name='fiberdb/lanrooms.html')),
    url(r'^lanrooms/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=LanRoom,
            template_name='fiberdb/lanrooms_detail.html')),
#    url(r'^lanrooms/add/$',
#        CreateView.as_view(
#            form_class=AddLanRoom,
#            model='LanRoom',
#            success_url='/lanrooms/',
#            template_name='fiberdb/lanrooms_add.html')),
    # Racks
    url(r'^racks/$',
        ListView.as_view(
            queryset=Rack.objects,
            context_object_name="rack_list",
            template_name='fiberdb/racks.html')),
    url(r'^racks/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Rack,
            template_name='fiberdb/racks_detail.html')),
#    url(r'^racks/add/$',
#        CreateView.as_view(
#            form_class=AddRack,
#            model='Rack',
#            success_url='/racks/',
#            template_name='fiberdb/racks_add.html')),
    # Boxes
    url(r'^boxes/$',
        ListView.as_view(
            queryset=Box.objects,
            context_object_name="box_list",
            template_name='fiberdb/boxes.html')),
    url(r'^boxes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Box,
            template_name='fiberdb/boxes_detail.html')),
#    url(r'^boxes/add/$',
#        CreateView.as_view(
#            form_class=AddBox,
#            model='Box',
#            success_url='/boxes/',
#            template_name='fiberdb/boxes_add.html')),
    # Adaptor Plates
    url(r'^adaptorplates/$',
        ListView.as_view(
            queryset=AdaptorPlate.objects,
            context_object_name="adaptorplate_list",
            template_name='fiberdb/adaptorplates.html')),
    url(r'^adaptorplates/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=AdaptorPlate,
            template_name='fiberdb/adaptorplates_detail.html')),
#    url(r'^adaptorplates/add/$',
#        CreateView.as_view(
#            form_class=AddAdaptorPlate,
#            model='AdaptorPlate',
#            success_url='/adaptorplates/',
#            template_name='fiberdb/adaptorplates_add.html')),
    # Adaptor Plate Connectors
    url(r'^adaptorplateconnectors/$',
        ListView.as_view(
            queryset=AdaptorPlateConnector.objects,
            context_object_name="adaptorplateconnector_list",
            template_name='fiberdb/adaptorplateconnectors.html')),
    url(r'^adaptorplateconnectors/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=AdaptorPlateConnector,
            template_name='fiberdb/adaptorplateconnectors_detail.html')),
#    url(r'^adaptorplateconnectors/add/$',
#        CreateView.as_view(
#            form_class=AddAdaptorPlateConnector,
#            model='AdaptorPlateConnector',
#            success_url='/adaptorplateconnectors/',
#            template_name='fiberdb/adaptorplateconnectors_add.html')),
    # Connector Type
    url(r'^connectortypes/$',
        ListView.as_view(
            queryset=ConnectorType.objects,
            context_object_name="connectortype_list",
            template_name='fiberdb/connectortypes.html')),
    url(r'^connectortypes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=ConnectorType,
            template_name='fiberdb/connectortypes_detail.html')),
#    url(r'^connectortypes/add/$',
#        CreateView.as_view(
#            form_class=AddConnectorType,
#            model='ConnectorType',
#            success_url='/connectortypes/',
#            template_name='fiberdb/connectortypes_add.html')),
    # Cable
    url(r'^cables/$',
        ListView.as_view(
            queryset=Cable.objects,
            context_object_name="cable_list",
            template_name='fiberdb/cables.html')),
    url(r'^cables/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Cable,
            template_name='fiberdb/cables_detail.html')),
   # Strand
    url(r'^strands/$',
        ListView.as_view(
            queryset=Strand.objects,
            context_object_name="strand_list",
            template_name='fiberdb/strands.html')),
    url(r'^strands/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Strand,
            template_name='fiberdb/strands_detail.html')),
   # Fiber Type
    url(r'^fibertypes/$',
        ListView.as_view(
            queryset=FiberType.objects,
            context_object_name="fibertype_list",
            template_name='fiberdb/fibertypes.html')),
    url(r'^fibertypes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=FiberType,
            template_name='fiberdb/fibertypes_detail.html')),
   # Path
    url(r'^paths/$',
        ListView.as_view(
            queryset=Path.objects,
            context_object_name="path_list",
            template_name='fiberdb/paths.html')),
    url(r'^paths/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Path,
            template_name='fiberdb/paths_detail.html')),
   # Point
    url(r'^points/$',
        ListView.as_view(
            queryset=Point.objects,
            context_object_name="point_list",
            template_name='fiberdb/points.html')),
    url(r'^points/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Point,
            template_name='fiberdb/points_detail.html')),
   # Point Type
    url(r'^pointtypes/$',
        ListView.as_view(
            queryset=PointType.objects,
            context_object_name="pointtype_list",
            template_name='fiberdb/pointtypes.html')),
    url(r'^pointtypes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=PointType,
            template_name='fiberdb/pointtypes_detail.html')),
)

urlpatterns += patterns('', 
    url(r'^admin/', include(admin.site.urls)),
)

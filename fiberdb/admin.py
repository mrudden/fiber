from fiberdb.models import *
from django.contrib import admin

class AdaptorPlateConnectorInline(admin.TabularInline):
    model = AdaptorPlateConnector
    Extra = 3

class AdaptorPlateInline(admin.TabularInline):
    model = AdaptorPlate
    Extra = 3

class BoxInline(admin.TabularInline):
    model = Box
    Extra = 3

class RackInline(admin.TabularInline):
    model = Rack
    Extra = 3

class LanRoomInline(admin.TabularInline):
    model = LanRoom
    Extra = 3

class AdaptorPlateAdmin(admin.ModelAdmin):
    inlines = [AdaptorPlateConnectorInline]

class BoxAdmin(admin.ModelAdmin):
    inlines = [AdaptorPlateInline]
    list_display = ('box_name', 'rack_id', 'date_added')

class RackAdmin(admin.ModelAdmin):
    inlines = [BoxInline]
    list_display = ('rack_name', 'lan_room_id', 'date_added')

class LanRoomAdmin(admin.ModelAdmin):
    inlines = [RackInline]
    list_display = ('lan_room_name', 'building_id', 'date_added')

class BuildingAdmin(admin.ModelAdmin):
    inlines = [LanRoomInline]
    list_display = ('short_name', 'building_name', 'date_added')

admin.site.register(Cable)
admin.site.register(Strand)
admin.site.register(ConnectorType)
admin.site.register(AdaptorPlateConnector)
admin.site.register(AdaptorPlate, AdaptorPlateAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Rack, RackAdmin)
admin.site.register(LanRoom, LanRoomAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(FiberType)
admin.site.register(Path)
admin.site.register(Point)
admin.site.register(PointType)

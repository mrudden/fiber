from fiberdb.models import *
from django.contrib import admin

class RackInline(admin. TabularInline):
    model = Rack
    Extra = 3

class LanRoomInline(admin.TabularInline):
    model = LanRoom
    Extra = 3

class LanRoomAdmin(admin.ModelAdmin):
    inlines = [RackInline]

class BuildingAdmin(admin.ModelAdmin):
    inlines = [LanRoomInline]


admin.site.register(Cable)
admin.site.register(Strand)
admin.site.register(ConnectorType)
admin.site.register(AdaptorPlateConnector)
admin.site.register(AdaptorPlate)
admin.site.register(Box)
admin.site.register(Rack)
admin.site.register(LanRoom, LanRoomAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(FiberType)
admin.site.register(Path)
admin.site.register(Point)
admin.site.register(PointType)

from django.forms import ModelForm, ModelChoiceField
from fiberdb.models import *

class AddBuilding(ModelForm):
    class Meta:
        model = Building

class AddLanRoom(ModelForm):
    class Meta:
        model = LanRoom

class AddRack(ModelForm):
#    building = ModelChoiceField(queryset=Building.objects, empty_label="Select a building")

    class Meta:
        model = Rack
#        fields = ('building', 'lan_room_id', 'rack_name')

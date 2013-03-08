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

class AddBox(ModelForm):
    class Meta:
        model = Box

class AddAdaptorPlate(ModelForm):
    class Meta:
        model = AdaptorPlate

class AddAdaptorPlateConnector(ModelForm):
    class Meta:
        model = AdaptorPlateConnector

class AddConnectorType(ModelForm):
    class Meta:
        model = ConnectorType

class AddCable(ModelForm):
    class Meta:
        model = Cable

class AddStrand(ModelForm):
    class Meta:
        model = Strand

class AddFiberType(ModelForm):
    class Meta:
        model = FiberType

class AddPath(ModelForm):
    class Meta:
        model = Path

class AddPoint(ModelForm):
    class Meta:
        model = Path

class AddPointType(ModelForm):
    class Meta:
        model = Path

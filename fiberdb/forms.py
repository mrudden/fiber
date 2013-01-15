from django.forms import ModelForm
from fiberdb.models import *

class AddBuilding(ModelForm):
    class Meta:
        model = Building

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from fiberdb.models import *

@dajaxice_register
def buildingcombo(request):
    dajax = Dajax()
    options = Building.objects
    out = []

    for option in options[int(option)]:
        out.append("<option value='#'>%s</option>" % option)

    dajax.assign('#buildings', 'innerHTML', ''.join(out))
    return dajax.json()

@dajaxice_register
def lanroomcombo(request, option):
    dajax = Dajax()
    options = LanRoom.objects.get(building_id=option)
    out = []
    
    for option in options[int(option)]:
        out.append("<option value='#'>%s</option>" % option)

    dajax.assign('#lanrooms', 'innerHTML', ''.join(out))
    return dajax.json()

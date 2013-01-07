from django.db import models

class Cable(models.Model):
    fiber_type_id = models.ForeignKey('FiberType')
    end1_box_id = models.ForeignKey('Box', related_name='end1_box')
    end2_box_id = models.ForeignKey('Box', related_name='end2_box')
    strands = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class Strand(models.Model):
    cable_id = models.ForeignKey('Cable')
    end1_plate_connector_id = models.ForeignKey('AdaptorPlateConnector', related_name= 'end1_adaptor_plate_connector')
    end2_plate_connector_id = models.ForeignKey('AdaptorPlateConnector', related_name= 'end2_adaptor_plate_connector')
    in_use = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class ConnectorType(models.Model):
    type = models.CharField(max_length=200)

class AdaptorPlateConnector(models.Model):
    adaptor_plate_id = models.ForeignKey('AdaptorPlate')
    connector_type_id = models.ForeignKey('ConnectorType')
    strand_position = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class AdaptorPlate(models.Model):
    box_id = models.ForeignKey('Box')
    box_position = models.CharField(max_length=200)
    alignment = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class Box(models.Model):
    rack_id = models.ForeignKey('Rack')
    box_name = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class Rack(models.Model):
    lan_room_id = models.ForeignKey('LanRoom')
    rack_name = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class LanRoom(models.Model):
    building_id = models.ForeignKey('Building')
    lan_room_name = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class Building(models.Model):
    building_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class FiberType(models.Model):
    fiber_type = models.CharField(max_length=200)
    micron = models.CharField(max_length=200)

class Path(models.Model):
    cable_id = models.ForeignKey('Cable')
    sequence = models.CharField(max_length=200)
    endpoint1_id = models.ForeignKey('Point', related_name= 'endpoint1')
    endpoint2_id = models.ForeignKey('Point', related_name= 'endpoint2')
#    date_added = models.DateTimeField('Date Added')

class Point(models.Model):
    point = models.CharField(max_length=200)
    point_type_id = models.ForeignKey('PointType')
    date_added = models.DateTimeField('Date Added')

class PointType(models.Model):
    point_type = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

from django.db import models

class Cable(models.Model):
    fiber_type_id = models.ForeignKey('FiberType')
    end1_box_id = models.ForeignKey('Box')
    end2_box_id = models.ForeignKey('Box')
    strands = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class Strand(models.Model):
    cable_id = models.ForeignKey('Cable')
    end1_plate_connector_id = models.ForeignKey('AdaptorPlateConnector')
    end2_plate_connector_id = models.ForeignKey('AdaptorPlateConnector')
    in_use = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')

class Connector_Type(models.Model):
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
    date_added = models.DateTimeField('Date Added')

class LanRoom(models.Model):
    date_added = models.DateTimeField('Date Added')

class Building(models.Model):
    date_added = models.DateTimeField('Date Added')

class FiberType(models.Model):
    fiber_type = models.CharField(max_length=200)
    micron = models.CharField(max_length=200)

class Path(models.Model):
    date_added = models.DateTimeField('Date Added')

class Point(models.Model):
    date_added = models.DateTimeField('Date Added')

class PointType(models.Model):
    date_added = models.DateTimeField('Date Added')

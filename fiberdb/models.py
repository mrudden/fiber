from django.db import models

class Building(models.Model):
    building_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['building_name']
    
    def __unicode__(self):
        return self.building_name
        
class LanRoom(models.Model):
    building_id = models.ForeignKey('Building')
    lan_room_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['building_id']

    def __unicode__(self):
        return self.building_id.__unicode__() + " - " + self.lan_room_name

class Rack(models.Model):
    lan_room_id = models.ForeignKey('LanRoom')
    rack_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['lan_room_id']

    def __unicode__(self):
        return self.rack_name
        
class Box(models.Model):
    rack_id = models.ForeignKey('Rack')
    box_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.box_name

class AdaptorPlate(models.Model):
    box_id = models.ForeignKey('Box')
    box_position = models.CharField(max_length=200)
    alignment = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.box_id.__unicode__() + " - " + self.box_position

class AdaptorPlateConnector(models.Model):
    adaptor_plate_id = models.ForeignKey('AdaptorPlate')
    connector_type_id = models.ForeignKey('ConnectorType')
    strand_position = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.strand_position

class ConnectorType(models.Model):
    type = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.type

class Cable(models.Model):
    fiber_type_id = models.ForeignKey('FiberType')
    end1_box_id = models.ForeignKey('Box', related_name='end1_box')
    end2_box_id = models.ForeignKey('Box', related_name='end2_box')
    strands = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "Strands: " + self.strands + ", Length: " + self.length

class Strand(models.Model):
    #strand_name = models.CharField(max_length=200)
    cable_id = models.ForeignKey('Cable')
    end1_plate_connector_id = models.ForeignKey('AdaptorPlateConnector', related_name= 'end1_adaptor_plate_connector')
    end2_plate_connector_id = models.ForeignKey('AdaptorPlateConnector', related_name= 'end2_adaptor_plate_connector')
    in_use = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
	#return self.strand_name
        return "End1: " + self.end1_plate_connector_id.__unicode__() + ", End2: " + self.end2_plate_connector_id.__unicode__() + ", Cable: " + self.cable_id.__unicode__()

class FiberType(models.Model):
    fiber_type = models.CharField(max_length=200)
    micron = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.fiber_type + " - " + self.micron

class Path(models.Model):
    cable_id = models.ForeignKey('Cable')
    sequence = models.CharField(max_length=200)
    endpoint1_id = models.ForeignKey('Point', related_name= 'endpoint1')
    endpoint2_id = models.ForeignKey('Point', related_name= 'endpoint2')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "End1: " + self.endpoint1_id.__unicode__() + " Sequence: " + self.sequence + " End2: " + self.endpoint2_id.__unicode__()

class Point(models.Model):
    point = models.CharField(max_length=200)
    point_type_id = models.ForeignKey('PointType')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.point 
#+ " - " + self.point_type_id.__unicode__()

class PointType(models.Model):
    point_type = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.point_type


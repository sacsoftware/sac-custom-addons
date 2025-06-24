from odoo import models , fields 

class InterventionTerrainA(models.Model):
    _name = 'intervention.terrain.a'
    _description = 'Intervention Terrain A'

    type_terrain = fields.Selection([('a' , 'Terrain A') , ('b' , 'Terrain B')] , string='Type de terrain' , default='a')
    name = fields.Char(string='Nom d`intervention')
    date_intervention = fields.Date(string='Date d`intervention')

class InterventionTerrainB(models.Model):
    _name = 'intervention.terrain.b'
    _description = 'Intervention Terrain B'

    type_terrain = fields.Selection([('a' , 'Terrain A') , ('b' , 'Terrain B')] , string='Type de terrain' , default='b')
    name = fields.Char(string='Nom d`intervention')
    date_intervention = fields.Date(string='Date d`intervention')


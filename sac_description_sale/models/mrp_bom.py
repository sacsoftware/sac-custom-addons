from odoo import models , fields

class MrpBom(models.Model):
    _inherit= 'mrp.bom'

    date_nomenclature = fields.Date(string='date de nomenclature')


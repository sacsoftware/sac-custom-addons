from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sac_description = fields.Char(string='Description sac')
    
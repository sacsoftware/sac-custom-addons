from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    reference_commande = fields.Char(string='Reference de la commande')
    
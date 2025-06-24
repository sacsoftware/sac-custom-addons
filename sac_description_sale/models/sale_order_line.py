from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    produit_description = fields.Text(string='Description du produit')
    date_description = fields.Date(string='Date de description')    

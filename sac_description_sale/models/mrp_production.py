from odoo import models, fields , api
from odoo.tools import float_compare

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    date_ordonnancement = fields.Date(string="Date d'ordonnancement")
    cause_retard = fields.Char(string='Cause de retard')
    rejected_quantity = fields.Integer(string='Quantité rejetée')
    facturation = fields.Char(string='Facturation')
    stock_arrete = fields.Integer(string='Stock pf arrêté')
    production_date = fields.Datetime(string="Date de production")
    cutting_date = fields.Date(string="Date de coupe")
    placement_comment = fields.Char(string="Commentaire placement" , size=200)
    cut_quantity = fields.Integer(string="Quantité coupée")
    orderly = fields.Boolean(string="Ordonnancée")
    compliance = fields.Selection([("Non_conforme","Non conforme"),
                                   ("Conforme","Conforme"),
                                   ("Conforme_derogation","Conforme avec dérogation")], string="Conformité")
    price_sheet = fields.Binary(string="Fiche prix", attachment=True)
    customer = fields.Many2one('res.partner',string="Client")
    assembly_quantity=fields.Integer(string="Assembled quantity")
    total_quantity=fields.Integer(string="Total quantity" , compute='compute_total_quantity' , store=True)
    manquant=fields.Text(string="Manquant", compute="compute_manquant", store=True)
    confirmation = fields.Selection(
        selection=[
            ("not_confirmed", "Pas Encore Confirmé"),
            ("confirm_manually", "Confirmé Manuellement")
            ],
            string="Confirmation",
            default="not_confirmed",
            required=True
            )




    @api.depends('assembly_quantity','cut_quantity')
    def compute_total_quantity(self):
        for record in self :
            record.total_quantity=record.assembly_quantity+record.cut_quantity

    @api.depends('state', 'reservation_state', 'date_planned_start', 'move_raw_ids', 'move_raw_ids.forecast_availability', 'move_raw_ids.forecast_expected_date', 'move_raw_ids.product_id','move_raw_ids.product_qty')
    def compute_manquant(self):
        list_manquant=[]
        for production in self :
            if production.state not in ('cancel', 'done', 'draft'):
                if any(float_compare(move.forecast_availability, 0 if move.state == 'draft' else move.product_qty, precision_rounding=move.product_id.uom_id.rounding) == -1 for move in production.move_raw_ids):
                    for move in production.move_raw_ids :
                        if float_compare(move.forecast_availability, 0 if move.state == 'draft' else move.product_qty, precision_rounding=move.product_id.uom_id.rounding) == -1:
                            list_manquant.append (move.product_id.display_name)
            production.manquant = ','.join(list_manquant)

    def action_confirm(self):
        res = super().action_confirm()
        for record in self:
            record.confirmation = 'confirm_manually'
        return res
            

from odoo import api, fields, models

class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    qr_code_data = fields.Char()
    barcode_value = fields.Char()
    last_known_location_id = fields.Many2one("stock.location")
    status = fields.Selection([
        ("filling","At Filling"),
        ("super_dealer","At Super Dealer"),
        ("dealer","At Dealer"),
        ("end_customer","With Customer"),
        ("lost","Lost"),
        ("maintenance","Maintenance"),
    ], default="filling")
    turnaround_days = fields.Float(compute="_compute_turnaround_days")

    def _compute_turnaround_days(self):
        for lot in self:
            lot.turnaround_days = 0.0


from odoo import api, fields, models

class OryxScanEvent(models.Model):
    _name = "oryx.scan.event"
    _description = "Scan Event"

    lot_id = fields.Many2one("stock.production.lot", required=True)
    operation_id = fields.Many2one("stock.picking")
    scan_type = fields.Selection([
        ("fill","Filling"),
        ("dispatch","Dispatch"),
        ("receipt","Receipt"),
        ("return","Return"),
        ("sale","Sale"),
        ("empty_return","Empty Return"),
    ], required=True)
    scanned_by = fields.Many2one("res.users", default=lambda self: self.env.user)
    timestamp = fields.Datetime(default=fields.Datetime.now)
    gps_lat = fields.Float()
    gps_lon = fields.Float()
    remarks = fields.Char()
    source_location_id = fields.Many2one("stock.location")
    dest_location_id = fields.Many2one("stock.location")
    delay_flag = fields.Boolean(default=False)

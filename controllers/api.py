
from odoo import http
from odoo.http import request

class OryxScanApi(http.Controller):
    @http.route('/oryx/api/scan', type='json', auth='api_key', methods=['POST'])
    def post_scan(self, **payload):
        events = payload.get('events', [])
        created = []
        for e in events:
            lot = request.env['stock.production.lot'].sudo().search([('name','=', e.get('serial'))], limit=1)
            if not lot:
                continue
            rec = request.env['oryx.scan.event'].sudo().create({
                'lot_id': lot.id,
                'scan_type': e.get('scan_type'),
                'gps_lat': e.get('gps_lat'),
                'gps_lon': e.get('gps_lon'),
                'remarks': e.get('remarks'),
                'source_location_id': e.get('source_location_id'),
                'dest_location_id': e.get('dest_location_id'),
            })
            created.append(rec.id)
        return {"status":"ok", "created": created}

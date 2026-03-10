
import json

from odoo import http
from odoo.http import request

class OryxScanApi(http.Controller):
    @http.route('/oryx/api/scan', type='http', auth='bearer', methods=['POST'], csrf=False, save_session=False)
    def post_scan(self, **kwargs):
        payload = request.httprequest.get_json(silent=True)
        if payload is None:
            try:
                payload = json.loads(request.httprequest.data or b'{}')
            except ValueError:
                return request.make_json_response({"status": "error", "message": "Invalid JSON payload"}, status=400)

        events = payload.get('events', [])
        if not isinstance(events, list):
            return request.make_json_response({"status": "error", "message": "events must be a list"}, status=400)

        created = []
        for e in events:
            if not isinstance(e, dict):
                continue

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
        return request.make_json_response({"status": "ok", "created": created})

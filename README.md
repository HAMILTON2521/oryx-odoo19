
# Oryx Cylinder Tracking (Odoo 19)

Minimal addon providing:
- Scan Event model + views
- Lot/Serial fields for QR & barcode data
- Simple label report (Code128 + QR)
- JSON endpoint `/oryx/api/scan`

## Running locally
1. Place the `oryx_cylinder_tracking` folder under your Odoo 19 `addons/` path.
2. Update Apps List and install **Oryx Cylinder Tracking**.
3. Ensure `barcodes` and `stock` are installed.

## Endpoint test
```
curl -X POST   -H "Content-Type: application/json"   -H "Authorization: Bearer <YOUR_API_KEY>"   -d '{"events":[{"serial":"CYN-00001234","scan_type":"dispatch","gps_lat":-6.792,"gps_lon":39.208}]}'   https://<your-odoo-domain>/oryx/api/scan
```

## Notes
- The endpoint uses `auth='api_key'`. Create an API key for the user in Odoo (My Profile → Account Security).
- For labels, set `barcode_value` and `qr_code_data` on each lot.

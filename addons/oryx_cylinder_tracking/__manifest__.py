
{
    "name": "Oryx Cylinder Tracking",
    "version": "19.0.1.0",
    "summary": "QR/Barcode-based tracking of LPG cylinders across checkpoints",
    "author": "SKT Tanzania Ltd",
    "depends": ["stock", "barcodes", "base"],
    "data": [
        "security/ir.model.access.csv",
        "views/scan_event_views.xml",
        "views/lot_views.xml",
        "views/actions_menus.xml",
        "reports/cylinder_label.xml"
    ],
    "license": "LGPL-3",
    "application": True
}

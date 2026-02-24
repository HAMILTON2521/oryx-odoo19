# Oryx Odoo 19 Project

This repository is structured for Odoo.sh deployment.

## Repository Layout

```
oryx-odoo19/
└─ addons/
   └─ oryx_cylinder_tracking/
```

The addon source and module-specific notes are in:
- `addons/oryx_cylinder_tracking/README.md`

## Odoo.sh Setup

1. Log in to Odoo.sh.
2. Create a new project.
3. Link this Git repository (`oryx-odoo19`).
4. Select the branch `main`.
5. Let Odoo.sh build the project and install/update apps.

## Local Development

1. Keep custom modules under `addons/`.
2. Update Apps List in Odoo.
3. Install **Oryx Cylinder Tracking**.

## Requirements

- Odoo 19
- Dependencies: `stock`, `barcodes`

# Custom PC Building Module Installation Guide

## Overview
This guide provides instructions for installing the Custom PC Building Module, version 1.0, on Odoo 16 Community Edition. This module allows users to configure and assemble custom personal computers through the Odoo backend and eCommerce website.

## Prerequisites
- Odoo 16 Community Edition installed and running
- Administrative access to the Odoo backend
- Access to the server's command line

## Installation Steps

### Step 1: Download the Module
Download the `custom_pc_building_module.zip` file from the provided source or repository.

### Step 2: Extract the Module
Extract the contents of the zip file to your Odoo addons directory, typically located at `/odoo/addons/`.

```bash
unzip custom_pc_building_module.zip -d /odoo/addons/
```

### Step 3: Update Module List
Log in to the Odoo backend as an administrator and navigate to `Apps > Update Apps List`. Click on 'Update Apps List' to refresh the list of available modules.

### Step 4: Install the Module
In the Odoo backend, search for 'Custom PC Building Module'. Click on the 'Install' button to begin the installation process.

### Step 5: Configure the Module
After installation, configure the module by setting up the following:
- `CUSTOM_PC_CATEGORY_ID` in the product category settings
- API credentials for real-time price and availability checks
- Budget management settings
- Compatibility check parameters

Refer to `doc/administrator_guide.md` for detailed configuration instructions.

### Step 6: Verify Installation
Verify that the module is installed correctly by navigating to the 'Custom PCs' category in the product management interface. Attempt to configure a custom PC to ensure all features are functioning.

### Step 7: Set Permissions
Set the appropriate user and manager permissions by importing the `security/ir.model.access.csv` and `security/custom_pc_security.xml` files through the Odoo backend settings.

### Step 8: Load Demo Data (Optional)
If you wish to load demo data for testing purposes, navigate to `Settings > Activate the developer mode`, then go to `Settings > Load a Translation` and import `demo/custom_pc_demo.xml`.

### Step 9: Run Tests (Optional)
To ensure the module's stability, run the tests provided in `tests/test_custom_pc.py`.

```bash
odoo-bin -c /etc/odoo.conf -d your_database --test-enable --stop-after-init --log-level=test -i custom_pc_building_module
```

## Troubleshooting
If you encounter any issues during installation, refer to `doc/troubleshooting_guide.md` for common problems and solutions.

## Support
For further assistance, contact the module development team or refer to the `README.md` file for support channels.

## Conclusion
The Custom PC Building Module should now be installed and ready for use. Enjoy configuring and selling custom PCs through your Odoo platform!

Remember to regularly check for updates to the module to ensure compatibility and access to the latest features.
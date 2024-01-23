import requests
from odoo import models, fields, api
from odoo.exceptions import UserError

class ExternalAPIIntegration(models.AbstractModel):
    _name = 'external.api.integration'
    _description = 'External API Integration for Custom PC Components'

    @api.model
    def get_vendor_data(self, component_type):
        """
        Fetch real-time price and availability data for PC components from vendor's API.
        :param component_type: Type of the PC component to fetch data for.
        :return: Dictionary with price and availability data.
        """
        # Placeholder for actual vendor API URL and API key
        vendor_api_url = "https://vendorapi.example.com/components"
        api_key = "YourVendorAPIKey"

        try:
            response = requests.get(
                vendor_api_url,
                params={'type': component_type},
                headers={'Authorization': f'Bearer {api_key}'}
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise UserError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            raise UserError(f"Error Connecting: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            raise UserError(f"Timeout error: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            raise UserError(f"An error occurred: {req_err}")

        data = response.json()
        price_availability_data = {
            'price': data.get('price'),
            'availability': data.get('availability'),
            'vendor': data.get('vendor')
        }
        return price_availability_data

    @api.model
    def update_component_prices(self):
        """
        Update the prices of the PC components in the system based on vendor data.
        """
        component_types = self.env['product.template'].search([('categ_id.name', '=', 'Custom PCs')])
        for component in component_types:
            vendor_data = self.get_vendor_data(component.name)
            component.write({
                'list_price': vendor_data['price'],
                'inventory_availability': 'in_stock' if vendor_data['availability'] else 'out_of_stock'
            })
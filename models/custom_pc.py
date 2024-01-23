from odoo import models, fields, api

class CustomPCComponent(models.Model):
    _name = 'custom.pc.component'
    _description = 'Custom PC Component'

    name = fields.Char(string='Component Name', required=True)
    category_id = fields.Many2one('product.category', string='Category', domain=[('id', '=', CUSTOM_PC_CATEGORY_ID)])
    price = fields.Float(string='Price')
    stock = fields.Integer(string='Stock')
    compatibility_details = fields.Text(string='Compatibility Details')

    @api.model
    def fetch_price_availability(self):
        # Placeholder for API integration logic
        # This method should be implemented in api/external_api_integration.py
        return ExternalAPIIntegration().get_vendor_data()

class CustomPCBuild(models.Model):
    _name = 'custom.pc.build'
    _description = 'Custom PC Build'

    name = fields.Char(string='Build Name', required=True)
    user_id = fields.Many2one('res.users', string='User')
    budget_limit = fields.Float(string='Budget Limit')
    components_ids = fields.Many2many('custom.pc.component', string='Components')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price')
    is_valid = fields.Boolean(string='Is Valid', compute='_compute_is_valid')

    @api.depends('components_ids.price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = sum(component.price for component in record.components_ids)

    @api.depends('components_ids')
    def _compute_is_valid(self):
        for record in self:
            record.is_valid = BuildValidator().validate_build(record.components_ids)

    def check_compatibility(self):
        # Placeholder for compatibility check logic
        # This method should be implemented in util/compatibility_checker.py
        return CompatibilityChecker().check_components(self.components_ids)

    def manage_budget(self, budget):
        # Placeholder for budget management logic
        # This method should be implemented in util/budget_manager.py
        self.budget_limit = budget
        return BudgetManager().manage_budget(self)

    def generate_order(self):
        # Placeholder for order generation logic
        # This method should be implemented in the sales module integration
        order_data = {
            'customer': self.user_id.partner_id.id,
            'order_lines': [(0, 0, {'product_id': component.id, 'price_unit': component.price}) for component in self.components_ids]
        }
        self.env['sale.order'].create(order_data)
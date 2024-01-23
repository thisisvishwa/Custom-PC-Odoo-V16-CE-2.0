from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PCBuilderWizard(models.TransientModel):
    _name = 'pc.builder.wizard'
    _description = 'Wizard for Building Custom PCs'

    custom_pc_build_id = fields.Many2one('custom.pc', string='Custom PC Build')
    component_ids = fields.Many2many('product.product', string='Components', domain=[('categ_id', '=', CUSTOM_PC_CATEGORY_ID)])
    budget_limit = fields.Float('Budget Limit')

    @api.onchange('component_ids')
    def _onchange_component_ids(self):
        if self.budget_limit and sum(self.component_ids.mapped('lst_price')) > self.budget_limit:
            return {
                'warning': {
                    'title': 'Budget Exceeded',
                    'message': BUDGET_EXCEEDED_MSG,
                }
            }

    def action_validate_build(self):
        self.ensure_one()
        build_validator = self.env['util.build_validator'].create({'build_id': self.custom_pc_build_id.id})
        validation_result = build_validator.validate()
        if validation_result.get('is_valid'):
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Validation Successful',
                    'message': 'The custom PC build is valid.',
                    'sticky': False,
                }
            }
        else:
            raise ValidationError(VALIDATION_ERROR_MSG)

    def action_check_compatibility(self):
        self.ensure_one()
        compatibility_checker = self.env['util.compatibility_checker'].create({'build_id': self.custom_pc_build_id.id})
        compatibility_result = compatibility_checker.check()
        if compatibility_result.get('is_compatible'):
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Compatibility Check',
                    'message': 'All components are compatible.',
                    'sticky': False,
                }
            }
        else:
            raise ValidationError(INCOMPATIBLE_COMPONENT_MSG.format(compatibility_result.get('message')))

    def action_generate_order(self):
        self.ensure_one()
        order_generator = self.env['util.order_generator'].create({'build_id': self.custom_pc_build_id.id})
        order = order_generator.generate()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Generated Order',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': order.id,
            'target': 'current',
        }
from odoo import http
from odoo.http import request

class CustomPCController(http.Controller):

    @http.route(['/shop/custom_pc/configure', '/shop/custom_pc/configure/<int:config_id>'], type='http', auth="public", website=True)
    def configure_custom_pc(self, config_id=None, **post):
        values = {
            'components': request.env['product.template'].search([('categ_id', '=', request.env.ref('custom_pc.CUSTOM_PC_CATEGORY_ID').id)]),
            'config_id': config_id,
            'budget_limit': post.get('budget_limit'),
            'session_key': CUSTOM_PC_CONFIG_SESSION_KEY,
        }
        return request.render('custom_pc.custom_pc_template', values)

    @http.route('/shop/custom_pc/price_availability', type='json', auth="public", methods=['POST'], website=True)
    def price_availability(self, **post):
        component_id = post.get('component_id')
        price_availability_data = request.env['custom_pc.api.external_api_integration'].getVendorData(component_id)
        return price_availability_data

    @http.route('/shop/custom_pc/manage_budget', type='json', auth="public", methods=['POST'], website=True)
    def manage_budget(self, **post):
        budget_limit = post.get('budget_limit')
        request.session[BUDGET_LIMIT_KEY] = budget_limit
        return {'success': True}

    @http.route('/shop/custom_pc/validate_build', type='json', auth="public", methods=['POST'], website=True)
    def validate_build(self, **post):
        build_data = post.get('build_data')
        validation_result = request.env['custom_pc.util.build_validator'].validateBuild(build_data)
        return validation_result

    @http.route('/shop/custom_pc/check_compatibility', type='json', auth="public", methods=['POST'], website=True)
    def check_compatibility(self, **post):
        component_ids = post.get('component_ids')
        compatibility_result = request.env['custom_pc.util.compatibility_checker'].checkCompatibility(component_ids)
        return compatibility_result

    @http.route('/shop/custom_pc/generate_order', type='http', auth="public", methods=['POST'], website=True)
    def generate_order(self, **post):
        build_data = post.get('build_data')
        order = request.env['custom_pc.util.order_generator'].generateOrder(build_data)
        return request.redirect('/shop/confirmation?order_id=%s' % order.id)
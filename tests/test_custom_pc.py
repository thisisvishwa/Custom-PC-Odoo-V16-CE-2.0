from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestCustomPC(TransactionCase):

    def setUp(self):
        super(TestCustomPC, self).setUp()
        self.CustomPC = self.env['custom.pc']
        self.PCBuilderWizard = self.env['pc.builder.wizard']
        self.CompatibilityChecker = self.env['util.compatibility_checker']
        self.BudgetManager = self.env['util.budget_manager']
        self.BuildValidator = self.env['util.build_validator']
        # Setup test data if needed

    def test_create_custom_pc(self):
        custom_pc_vals = {
            'name': 'Test Custom PC',
            'category_id': self.ref('product.' + CUSTOM_PC_CATEGORY_ID),
        }
        custom_pc = self.CustomPC.create(custom_pc_vals)
        self.assertTrue(custom_pc, "Custom PC was not created")

    def test_budget_management(self):
        budget_manager = self.BudgetManager.create({'budget_limit': 1000.0})
        self.assertEqual(budget_manager.budget_limit, 1000.0, "Budget limit was not set correctly")

    def test_build_validation(self):
        custom_pc_vals = {
            'name': 'Test Custom PC',
            'category_id': self.ref('product.' + CUSTOM_PC_CATEGORY_ID),
        }
        custom_pc = self.CustomPC.create(custom_pc_vals)
        with self.assertRaises(ValidationError):
            self.BuildValidator.validateBuild(custom_pc)

    def test_compatibility_check(self):
        compatibility_checker = self.CompatibilityChecker.create({})
        result = compatibility_checker.checkCompatibility({})
        self.assertIsInstance(result, dict, "Compatibility check did not return a dictionary")

    def test_order_generation(self):
        custom_pc_vals = {
            'name': 'Test Custom PC',
            'category_id': self.ref('product.' + CUSTOM_PC_CATEGORY_ID),
        }
        custom_pc = self.CustomPC.create(custom_pc_vals)
        order = self.PCBuilderWizard.generateOrder(custom_pc)
        self.assertTrue(order, "Order was not generated")

    def test_real_time_price_availability(self):
        component = self.env['product.product'].create({
            'name': 'Test Component',
            'type': 'consu',
        })
        self.ExternalAPIIntegration = self.env['api.external_api_integration']
        price_availability_data = self.ExternalAPIIntegration.getVendorData(component)
        self.assertIsInstance(price_availability_data, dict, "Price and availability data is not a dictionary")
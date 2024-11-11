from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

class TestMaterialOrder(TransactionCase):

    def setUp(self):
        super(TestMaterialOrder, self).setUp()
        self.MaterialOrder = self.env['kt.material.order']

    def test_buy_price_above_minimum(self):
        # Test case where buy_price is valid (>= 100)
        product = self.MaterialOrder.create({
            'kt_name': 'Produk A',
            'kt_code': 'A001',
            'kt_currency_id': 1, # EUR currency default
            'kt_buy_price': 150,
            'kt_supplier_id': 14, # Azure Interior from demo data
            'kt_type': 'fabric',
        })
        self.assertEqual(product.buy_price, 150, "Buy price harusnya 150")

    def test_buy_price_below_minimum(self):
        # Test case where buy_price is below 100, should raise ValidationError
        with self.assertRaises(UserError):
            self.MaterialOrder.create({
            'kt_name': 'Produk A',
            'kt_code': 'A001',
            'kt_currency_id': 1, # EUR currency default
            'kt_buy_price': 50, 
            'kt_supplier_id': 14, # Azure Interior from demo data
            'kt_type': 'cotton',
        })

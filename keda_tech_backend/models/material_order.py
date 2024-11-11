from odoo import api, models, exceptions, fields, _
from odoo.exceptions import UserError

# KT as nickname for Keda tech
# _id for Many2one standard field name
# _ids for Many2many or One2many standard field name
class MaterialOrder(models.Model):
	_name = 'kt.material.order'
	_rec_name = 'kt_name'

	kt_name = fields.Char(string='Material Name', required=True)
	kt_code = fields.Char(string='Material Code', required=True)
	kt_type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')], string='Material Type', required=True)
	kt_currency_id = fields.Many2one('res.currency', string='Currency', required=True)
	kt_buy_price = fields.Monetary(string='Buy Price', currency_field='kt_currency_id', required=True)
	kt_supplier_id = fields.Many2one('res.partner', string='Related Supplier', required=True)

	@api.model
	def create(self, vals):
		if vals.get('kt_buy_price', 0) < 100:
			raise UserError("Buy Price can not be under 100!")
		return super(MaterialOrder, self).create(vals)
	
	def write(self, values):
		res = super(MaterialOrder, self).write(values)
		if 'kt_buy_price' in values:
			if self.kt_buy_price < 100:
				raise UserError('Buy Price can not be under 100!')
		return res
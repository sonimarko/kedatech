from odoo import http
from odoo.http import request

from odoo import http
from odoo.http import request
import json

class MaterialOrderController(http.Controller):
    @http.route('/get_fabric_material', type='http', auth='public', methods=['GET'], csrf=False)
    def get_fabric_material(self):
        material_orders = request.env['kt.material.order'].sudo().search_read(
            [('kt_type', '=', 'fabric')],
            ['kt_name', 'kt_code', 'kt_type', 'kt_buy_price', 'kt_supplier_id'],
            order='kt_name asc'
        )
        result = [{
            'name': order['kt_name'],
            'code': order['kt_code'],
            'type': order['kt_type'],
            'buy_price': order['kt_buy_price'],
            'supplier': order['kt_supplier_id'][1] if order['kt_supplier_id'] else "Unknown",
        } for order in material_orders]

        return request.make_response(json.dumps(result), headers=[('Content-Type', 'application/json')])
    
    @http.route('/get_cotton_material', type='http', auth='public', methods=['GET'], csrf=False)
    def get_cotton_material(self):
        material_orders = request.env['kt.material.order'].sudo().search_read(
            [('kt_type', '=', 'cotton')],
            ['kt_name', 'kt_code', 'kt_type', 'kt_buy_price', 'kt_supplier_id'],
            order='kt_name asc'
        )
        result = [{
            'name': order['kt_name'],
            'code': order['kt_code'],
            'type': order['kt_type'],
            'buy_price': order['kt_buy_price'],
            'supplier': order['kt_supplier_id'][1] if order['kt_supplier_id'] else "Unknown",
        } for order in material_orders]

        return request.make_response(json.dumps(result), headers=[('Content-Type', 'application/json')])
    
    @http.route('/get_jeans_material', type='http', auth='public', methods=['GET'], csrf=False)
    def get_jeans_material(self):
        material_orders = request.env['kt.material.order'].sudo().search_read(
            [('kt_type', '=', 'jeans')],
            ['kt_name', 'kt_code', 'kt_type', 'kt_buy_price', 'kt_supplier_id'],
            order='kt_name asc'
        )
        result = [{
            'name': order['kt_name'],
            'code': order['kt_code'],
            'type': order['kt_type'],
            'buy_price': order['kt_buy_price'],
            'supplier': order['kt_supplier_id'][1] if order['kt_supplier_id'] else "Unknown",
        } for order in material_orders]

        return request.make_response(json.dumps(result), headers=[('Content-Type', 'application/json')])
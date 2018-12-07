# -*- coding: utf-8 -*-
from odoo import http

# class Src/user/odooDevTraning(http.Controller):
#     @http.route('/src/user/odoo_dev_traning/src/user/odoo_dev_traning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/src/user/odoo_dev_traning/src/user/odoo_dev_traning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('src/user/odoo_dev_traning.listing', {
#             'root': '/src/user/odoo_dev_traning/src/user/odoo_dev_traning',
#             'objects': http.request.env['src/user/odoo_dev_traning.src/user/odoo_dev_traning'].search([]),
#         })

#     @http.route('/src/user/odoo_dev_traning/src/user/odoo_dev_traning/objects/<model("src/user/odoo_dev_traning.src/user/odoo_dev_traning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('src/user/odoo_dev_traning.object', {
#             'object': obj
#         })
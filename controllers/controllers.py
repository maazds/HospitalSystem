# -*- coding: utf-8 -*-
# from odoo import http


# class HopitalSystem(http.Controller):
#     @http.route('/hopital_system/hopital_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hopital_system/hopital_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hopital_system.listing', {
#             'root': '/hopital_system/hopital_system',
#             'objects': http.request.env['hopital_system.hopital_system'].search([]),
#         })

#     @http.route('/hopital_system/hopital_system/objects/<model("hopital_system.hopital_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hopital_system.object', {
#             'object': obj
#         })

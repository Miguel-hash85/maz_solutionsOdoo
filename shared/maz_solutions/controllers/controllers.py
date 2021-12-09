# -*- coding: utf-8 -*-
from odoo import http

# class MazSolutions(http.Controller):
#     @http.route('/maz_solutions/maz_solutions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maz_solutions/maz_solutions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('maz_solutions.listing', {
#             'root': '/maz_solutions/maz_solutions',
#             'objects': http.request.env['maz_solutions.maz_solutions'].search([]),
#         })

#     @http.route('/maz_solutions/maz_solutions/objects/<model("maz_solutions.maz_solutions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maz_solutions.object', {
#             'object': obj
#         })
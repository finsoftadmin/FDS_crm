# -*- coding: utf-8 -*-
# from odoo import http


# class FdsCrm(http.Controller):
#     @http.route('/fds_crm/fds_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fds_crm/fds_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fds_crm.listing', {
#             'root': '/fds_crm/fds_crm',
#             'objects': http.request.env['fds_crm.fds_crm'].search([]),
#         })

#     @http.route('/fds_crm/fds_crm/objects/<model("fds_crm.fds_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fds_crm.object', {
#             'object': obj
#         })

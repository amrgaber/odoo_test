# -*- coding: utf-8 -*-
from odoo import http

# class GithubProj(http.Controller):
#     @http.route('/github_proj/github_proj/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/github_proj/github_proj/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('github_proj.listing', {
#             'root': '/github_proj/github_proj',
#             'objects': http.request.env['github_proj.github_proj'].search([]),
#         })

#     @http.route('/github_proj/github_proj/objects/<model("github_proj.github_proj"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('github_proj.object', {
#             'object': obj
#         })
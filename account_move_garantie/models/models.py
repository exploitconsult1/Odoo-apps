from odoo import models, fields, api

class res_company_inherit(models.Model):
    _inherit = 'res.company'
    _description = 'res.company.inherit'

    description = fields.Text(string="Description facture")
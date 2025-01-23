from odoo import models, fields

class UavtMahalle(models.Model):
    _name = 'uavt.mahalle'
    _description = 'District'

    name = fields.Char(string='Name', required=True)
    koy_id = fields.Many2one('uavt.koy', string='Village', required=True)
    kod = fields.Integer(string='Code', required=True)

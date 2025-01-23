from odoo import models, fields, api

class UavtKoy(models.Model):
    _name = 'uavt.koy'
    _description = 'Village'

    name = fields.Char(string='Name', required=True)
    ilce_id = fields.Many2one('uavt.ilce', string='County', required=True)
    kod = fields.Integer(string='Code', required=True)
    sirano = fields.Integer(string='Order Number', required=True)
    koyad = fields.Char(string='Village Name')
    koykod = fields.Integer(string='Village Code')
    ilce_kod = fields.Integer(related='ilce_id.ilce_kod', store=True, string='County Code')

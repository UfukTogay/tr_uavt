from odoo import models, fields, api

class UavtKoy(models.Model):
    _name = 'uavt.koy'
    _description = 'Village'

    name = fields.Char(string='Name', required=True)
    ilce_id = fields.Many2one('uavt.ilce', string='County', required=True)
    uavt_kodu = fields.Integer(string='UAVT Code', required=True)  # Changed from kod
    sirano = fields.Integer(string='Order Number', required=True)
    koyad = fields.Char(string='Village Name')
    koykod = fields.Integer(string='Village Code')
    ilce_kod = fields.Integer(related='ilce_id.uavt_kodu', store=True, string='County Code')  # Changed from ilce_kod

from odoo import models, fields

class UavtSokak(models.Model):
    _name = 'uavt.sokak'
    _description = 'Street'

    name = fields.Char(string='Name', required=True)
    mahalle_id = fields.Many2one('uavt.mahalle', string='Neighborhood', required=True)
    kod = fields.Integer(string='Code', required=True)
    sokak_turu = fields.Char(string='Street Type')
    sokak_turu_aciklama = fields.Char(string='Street Type Description')
    gelisim_durumu_aciklama = fields.Char(string='Development Status Description')
    gelisim_durumu_kodu = fields.Char(string='Development Status Code')
    sabit_tanitim_numarasi = fields.Float(string='Fixed Identification Number')

from operator import index
from odoo import models, fields, api

class UavtIlce(models.Model):
    _name = 'uavt.ilce'
    _description = 'County'

    name = fields.Char(string='Name', required=True, index=True)
    _sql_constraints = [
        ('unique_name_il', 'UNIQUE(name, il_kod)', 'County name must be unique per city!')
    ]
    il_kod = fields.Many2one('res.country.state', string='City', required=True, index=True,
                            domain="[('country_id.code', '=', 'TR')]")
    uavt_kodu = fields.Integer(string='UAVT Code', required=True)

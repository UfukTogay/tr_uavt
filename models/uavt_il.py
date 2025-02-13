from odoo import models, fields

class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    ilce_ids = fields.One2many('uavt.ilce', 'il_kod', string='Counties')
    ilce_count = fields.Integer(string='County Count', compute='_compute_ilce_count')

    def _compute_ilce_count(self):
        for state in self:
            state.ilce_count = len(state.ilce_ids)

from odoo import models, fields, api

class UavtIlce(models.Model):
    _name = 'uavt.ilce'
    _description = 'County'

    name = fields.Char(string='Name', required=True)
    il_kod = fields.Many2one('res.country.state', string='City', required=True,
                            domain="[('country_id.code', '=', 'TR')]",
                            default=lambda self: self.env['res.country.state'].search(
                                [('country_id.code', '=', 'TR')], limit=1))
    kod = fields.Integer(string='Code', required=True)
    ilce_kod = fields.Integer(string='County Code', compute='_compute_ilce_kod', store=True)

    @api.depends('kod')
    def _compute_ilce_kod(self):
        for record in self:
            record.ilce_kod = record.kod

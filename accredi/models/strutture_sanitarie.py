from odoo import fields, models, api

class struttura_sanitaria(models.Model):
   _inherit = "res.partner"

   struttura_sanitaria = fields.Boolean("è una struttura sanitaria?")
   accreditamento = fields.Boolean("è accreditata?")

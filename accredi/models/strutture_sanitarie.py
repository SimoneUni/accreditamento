from odoo import fields, models, api

class struttura_sanitaria(models.Model):
   _inherit = "res.partner"

   struttura_sanitaria = fields.Boolean("è una struttura sanitaria?", compute="_compute_struttura_sanitaria")
   accreditamento = fields.Boolean("è accreditata?")
   is_company = fields.Boolean(default=True)

   @api.onchange('is_company')
   def _onchange_is_company(self):
      if self.is_company:
         self.struttura_sanitaria = True
      else:
         self.struttura_sanitaria = False

   @api.depends('is_company')
   def _compute_struttura_sanitaria(self):
      for record in self:
         record.struttura_sanitaria = record.is_company
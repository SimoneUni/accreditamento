from odoo import fields, models, api

class struttura_sanitaria(models.Model):
   _inherit = "res.partner"

   struttura_sanitaria = fields.Boolean("è una struttura sanitaria?", readonly=False)
   accreditamento = fields.Boolean("è accreditata?")
   is_company = fields.Boolean(default=True)

   @api.onchange('is_company')
   def _onchange_is_company(self):
      for record in self:
         if record._origin:  # Verifica se il record è un record esistente
            continue
         if record.is_company:
            record.struttura_sanitaria = True
         else:
            record.struttura_sanitaria = False



   @api.model
   def create(self, vals):
      # Verifica se il record sta per essere creato come contatto
      if vals.get('is_company') and not vals.get('struttura_sanitaria', False):
         # Impedisce l'esecuzione della logica se il record è un contatto
         return super(struttura_sanitaria, self).create(vals)
      else:
         return super(struttura_sanitaria, self).create(vals)
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

   @api.model
   def create(self, vals):
      # Controlla se il record sta per essere creato come azienda (is_company=True)
      if vals.get('is_company'):
         vals['struttura_sanitaria'] = False  # Impostare su False per i nuovi contatti azienda
      return super(struttura_sanitaria, self).create(vals)

   def write(self, vals):
      # Controlla se il record sta per essere aggiornato con is_company=True
      if 'is_company' in vals and vals['is_company']:
         vals['struttura_sanitaria'] = True  # Impostare su True quando si aggiorna un contatto azienda
      return super(struttura_sanitaria, self).write(vals)
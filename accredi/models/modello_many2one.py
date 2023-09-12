from odoo import fields, models

class modello_many2one(models.Model):
    _name = "pratiche"
    _description = "Descrizione"
    _rec_name = 'tipo_pratica'

    tipo_pratica = fields.Char(
        string="Tipologia pratica",
        required=True)







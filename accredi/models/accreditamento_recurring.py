from odoo import models, fields, api



class TestModel(models.Model):
    _name = 'test_model'
    _description = "Test Model"
    _inherit = ['mail.thread','mail.activity.mixin']


    descri = fields.Text(string="Descrizione")
    Incremento = fields.Integer(default=0)  # Cambiato in Integer
    identificativo = fields.Char(string="Codice del Record", compute='_compute_display_code', store=True)
    booleano = fields.Boolean()
    status = fields.Selection([('in_compilazione','In compilazione'),('da_approvare','Da approvare'),
                               ('approvata','Approvata'), ('rifiutato','Cancellata')],
                              string="Status", default="in_compilazione",  tracking=True)
    tipologia_pratica_id = fields.Many2one("pratiche", string="Tipo di pratica")
    autore_registrazione_id = fields.Many2one("res.users", string="Autore Registrazione" , default=lambda self: self.env.user)

    name = fields.Char(string="ID", compute='_compute_name', store=True, readonly=True)
    struttura_sanitaria_id = fields.Many2one('res.partner', string="è una struttura sanitaria?")
    year_pratica = fields.Integer(string="Anno di registrazione", compute='_compute_year_pratica', store=True)
    richiedente_id = fields.Many2one("res.partner",  string="Richiedente", domain=[('is_company','=', False),('struttura_sanitaria','=', False)], required=True)
    struttura_da_accreditare = fields.Many2one("res.partner", string="Struttura da accreditare", domain=[('accreditamento','=', False),('is_company','=',True),('struttura_sanitaria','=', True)], required=True)


    def pulsante_da_conferma(self):
        self.status="da_approvare"
        self.message_post(body="Confermato!")
    def pulsante_da_approvare(self):
            self.status = "approvata"
            self.message_post(body="Approvato!")
    def pulsante_rigetto(self):
            self.status = "rifiutato"
            self.message_post(body="Rifiutato!")


    def pulsante_per_back(self):
            self.status = "in_compilazione"
            self.message_post(body="Indietro!")
    @api.depends('Incremento')
    def _compute_display_code(self):
        for record in self:
            year = fields.Date.today().year  # Ottieni l'anno corrente
            record.identificativo = f'ACR/{year}/{str(record.Incremento).zfill(3)}'

    @api.model
    def create(self, vals):
        if vals.get('Incremento', 0) == 0:
            # Trova il massimo valore di Incremento nella tabella
            max_incremento = self.search([], order="Incremento desc", limit=1)
            new_incremento = max_incremento.Incremento + 1 if max_incremento else 1
            vals['Incremento'] = new_incremento
            vals['name'] = f'ACR/{fields.Date.today().year}/{str(new_incremento).zfill(3)}'
        else:
            vals['name'] = f'ACR/{fields.Date.today().year}/{str(vals["Incremento"]).zfill(3)}'

        return super(TestModel, self).create(vals)

    def message_post(self, body):
        pass

    def _compute_year_pratica(self):
        for record in self:
            record.year_pratica = fields.Date.today().year







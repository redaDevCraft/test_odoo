from odoo import models, fields

class TestModel(models.Model):
    _name = 'testmodel.test' 
    _description = 'TEST'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    
    patient_id = fields.Many2one('patient.test',string='Les patients')
    pharmacie_id = fields.Many2one('pharmacie.test',string='Les pharmacies')

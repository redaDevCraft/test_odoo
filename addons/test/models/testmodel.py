from odoo import models, fields

class TestModel(models.Model):
    _name = 'testmodel.test' 
    _description = 'TEST'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)

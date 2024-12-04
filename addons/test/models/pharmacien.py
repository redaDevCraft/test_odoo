from odoo import models, fields,api

class Pharmacien(models.Model):
    _name = 'pharmacien.test' 
    _description = 'Pharmacien'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    telephone = fields.Integer(string='Telephone')
    pharmacie_id = fields.Many2one('pharmacie.test',string='Nom du Pharmacie')
    

from odoo import models, fields,api

class Pharmacie(models.Model):
    _name = 'pharmacie.test' 
    _description = 'Pharmacie'

    nom = fields.Char(string='Nom', required=True)
    adresse = fields.Char(string='adresse')
    nbr_patient = fields.Integer(string='Nombre de patients')
    pharmacien_ids =fields.One2many('pharmacien.test','pharmacie_id',string='Les pharmaciens')
    
    test_assoc_ids= fields.One2many('testmodel.test','pharmacie_id',string='Les pharmaciens')

    

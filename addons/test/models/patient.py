from odoo import models, fields,api
from dateutil.relativedelta import relativedelta
from datetime import date


class Patient(models.Model):
    _name = 'patient.test' 
    _description = 'patient'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    age = fields.Integer(string='Age')
    date_naissanse = fields.Date(string='Date de naissance')
    
    test_assoc_ids= fields.One2many('testmodel.test','patient_id',string='Les pharmaciens')
    
    @api.onchange('date_naissanse')
    def calcule_age(self):
        for record in self:
            if record.date_naissanse:
                date_n = record.date_naissanse
                d2 = date.today()
                rd = relativedelta(d2, date_n)
                record.age = rd.years
           
                    


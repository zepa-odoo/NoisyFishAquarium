from odoo import models, fields

class User(models.Model):
    _name = "user"
    _description = "which store the differance type of users"

    name = fields.Char(required=True)

    

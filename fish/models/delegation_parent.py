from odoo import fields, models

class DelegationParent(models.Model):
    _name = "delegation.parent"
    _description = "parent"

    name = fields.Char()
    age = fields.Integer()
    details = fields.Text()
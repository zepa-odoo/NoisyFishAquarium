from odoo import fields,models

class Order(models.Model):
    _name = "order"
    _description = "order details"

    name = fields.Char(required=True)
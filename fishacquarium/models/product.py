from odoo import fields,models

class Product(models.Model):
    _name = "product"
    _description = "Products for acquarium"

    name = fields.Char(required=True)
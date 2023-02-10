from odoo import fields,models

class ProductColor(models.Model):
    _name = "product.color"
    _description = "colors"

    name = fields.Char(required=True)
    color_value = fields.Char()
from odoo import fields,models

class ProductColor(models.Model):
    _name = "product.color"
    _description = "colors"

    name = fields.Char(required=True, inverse="_inverse_name")
    color_value = fields.Char()

    _sql_constraints = [
        ('product_color_checker', 'unique(name)', 'This type is already available.')
    ]
    
    # @api.depends('name')
    def _inverse_name(self):
        for record in self:
            record.name = record.name.title()
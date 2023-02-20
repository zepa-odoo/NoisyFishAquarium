from odoo import fields,models

class ProductCategoryFish(models.Model):
    _name = "product.category.fish"
    _description = "fish category"

    name = fields.Char(required=True, inverse="_inverse_name")

    _sql_constraints = [
        ('product_fish_checker', 'unique(name)', 'This type is already available.')
    ]
    
    # @api.depends('name')
    def _inverse_name(self):
        for record in self:
            record.name = record.name.title()
from odoo import fields,models

class ProductCategoryFood(models.Model):
    _name = "product.category.food"
    _description = "food category"

    name = fields.Char(required=True, inverse="_inverse_name")

    _sql_constraints = [
        ('product_food_checker', 'unique(name)', 'This type is already available.')
    ]
    
    # @api.depends('name')
    def _inverse_name(self):
        for record in self:
            record.name = record.name.title()
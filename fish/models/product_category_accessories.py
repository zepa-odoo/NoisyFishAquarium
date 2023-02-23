from odoo import fields,models

class ProductCategoryAccessories(models.Model):
    _name = "product.category.accessories"
    _description = "accessories category"

    name = fields.Char(required=True, inverse="_inverse_name")

    _sql_constraints = [
        ('product_accessories_checker', 'unique(name)', 'This type is already available.')
    ]
    
    # @api.depends('name')
    def _inverse_name(self):
        for record in self:
            record.name = record.name.title()
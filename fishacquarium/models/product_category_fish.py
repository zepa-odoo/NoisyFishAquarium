from odoo import fields,models

class ProductCategoryFish(models.Model):
    _name = "product.category.fish"
    _description = "fish category"

    name = fields.Char(required=True)
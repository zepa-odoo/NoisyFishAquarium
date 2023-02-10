from odoo import fields,models

class ProductCategoryFood(models.Model):
    _name = "product.category.food"
    _description = "food category"

    name = fields.Char(required=True)
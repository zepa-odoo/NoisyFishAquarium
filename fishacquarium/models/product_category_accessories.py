from odoo import fields,models

class ProductCategoryAccessories(models.Model):
    _name = "product.category.accessories"
    _description = "accessories category"

    name = fields.Char(required=True)
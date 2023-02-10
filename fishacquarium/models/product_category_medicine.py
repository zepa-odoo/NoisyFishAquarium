from odoo import fields,models

class ProductCategoryMedicine(models.Model):
    _name = "product.category.medicine"
    _description = "medicine category"

    name = fields.Char(required=True)
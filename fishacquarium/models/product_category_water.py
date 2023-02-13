from odoo import fields,models

class ProductCategoryWater(models.Model):
    _name = "product.category.water"
    _description = "water category"

    name = fields.Char(required=True,string="Type")
    water_ph = fields.Integer(string="PH")
    water_temperature = fields.Float(string="Temperature")

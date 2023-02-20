from odoo import fields,models

class ProductCategoryWater(models.Model):
    _name = "product.category.water"
    _description = "water category"

    name = fields.Char(required=True,string="Type", inverse="_inverse_name")
    water_ph = fields.Integer(string="PH")
    water_temperature = fields.Float(string="Temperature")

    
    
    # @api.depends('name')
    def _inverse_name(self):
        for record in self:
            record.name = record.name.title()

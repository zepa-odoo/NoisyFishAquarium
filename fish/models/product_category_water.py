from odoo import fields,models,api

class ProductCategoryWater(models.Model):
    _name = "product.category.water"
    _description = "water category"
    

    name = fields.Char(required=True,string="Type", compute="_compute_name",readonly=False,store=True)
    water_ph = fields.Float(string="PH") # 0 -14 range
    water_temperature = fields.Float(string="Temperature")
    

    _sql_constraints = [
        (
            'check_water_ph',
            'CHECK(water_ph > 0.0 and water_ph<14.0)',
            "Water PH range is 0 to 14 only ."
        )
    ]
    
    
    @api.depends('name')
    def _compute_name(self):
        for record in self:
            record.name = record.name.title()

    
    
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "ph-%s- %s" % (record.water_ph, record.name or '')))
        return result


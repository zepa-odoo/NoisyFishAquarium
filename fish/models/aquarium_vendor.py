from odoo import models,fields

class AquariumVendor(models.Model):
    _name="aquarium.vendor"
    _description = "All suppliers for the product"

    company_id = fields.Many2one("res.company")
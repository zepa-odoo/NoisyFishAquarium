from odoo import models,fields,api
from datetime import datetime

class AquariumVendor(models.Model):
    _name="aquarium.vendor"
    _description = "All suppliers for the product"
    _rec_name = "company_id"

    company_id = fields.Many2one("res.company")

    product_production_type = fields.Selection(
        string = "Production Type",
        selection = [('natural_product','Natural Product'),('artificial_product','Artificial Product'),('both','Both Artificial & Natural')],
        help  = "Select which type of product produce"
        )
    company_year=fields.Selection(selection='years_selection',
        string="Foundation Year")
    
    experiance = fields.Integer(string="Experiance",compute="_compute_experiance", store=True)

    def years_selection(self):
        year_list=[]
        for y in range(datetime.now().year-30, datetime.now().year):
            year_list.append((str(y), str(y)))
        return year_list
    
    @api.depends('company_year')
    def _compute_experiance(self):
        for record in self:
            if record.create_date:
                record.experiance = fields.date.today().year-int(record.company_year)
            else:
                record.experiance=0
from odoo import models,fields,api
from datetime import datetime

class AquariumVendor(models.Model):
    _name="aquarium.vendor"
    _description = "All suppliers for the product"
    _rec_name = "company_id"

    company_id = fields.Many2one("res.company")

    phone_no= fields.Char(string="Contact No(M)", related = "company_id.phone", store=True, readonly=False)
    email = fields.Char(string="Email", related = "company_id.email", store=True, readonly=False)
    website = fields.Char(string="Website", related = "company_id.website", store=True, readonly=False)

    street = fields.Char(string="Address", related = "company_id.street", store=True, readonly=False)
    street_2 = fields.Char (related = "company_id.street2", store=True, readonly=False)
    city = fields.Char(related = "company_id.city", store=True, readonly=False)
    zip = fields.Char(related = "company_id.zip", store=True, readonly=False)
    state_id = fields.Many2one( related = "company_id.state_id", store=True, readonly=False)
    country_id = fields.Many2one( related = "company_id.country_id", store=True, readonly=False)
    logo = fields.Binary(related = "company_id.logo", readonly=False)
    company_details = fields.Html(string ="Company Details", related = "company_id.company_details", readonly=False )


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
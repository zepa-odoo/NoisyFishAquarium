from odoo import fields,models, api
from datetime import datetime

class ProductVendor(models.Model):
    _name = "product.vendor"
    _description = "All suppliers for the product"

    name = fields.Char(required="True", string="Company Name")
    phone_no = fields.Char(string="Contact No(M)")
    company_address = fields.Text(string="Address")
    company_email = fields.Char(string="Email")
    brand_name = fields.Char(string="Brand Name")
    description = fields.Text(string="Foundation Description")
    brand_img = fields.Image(string="Brand Image", max_width=70, max_height=70)
    experiance = fields.Integer(string="Experiance",compute="_compute_experiance")
    product_production_type = fields.Selection(
        string = "Production Type",
        selection = [('natural_product','Natural Product'),('artificial_product','Artificial Product')],
        help  = "Select which type of product produce"
        )
    company_year=fields.Selection(selection='years_selection',
        string="Foundation Year")
    
    
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
                
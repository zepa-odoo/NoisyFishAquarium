from odoo import fields,models

class ProductVendor(models.Model):
    _name = "product.vendor"
    _description = "All suppliers for the product"

    name = fields.Char(required="True", string="Company Name")
    phone_no = fields.Integer(string="Contact No(M)")
    company_address = fields.Text(string="Address")
    company_email = fields.Char(string="Email")
    brand_name = fields.Char(string="Brand Name")
    product_production_type = fields.Selection(
        string = "Production Type",
        selection = [('natural_product','Natural Product'),('artificial_product','Artificial Product')],
        help  = "Select which type of product produce"
        )
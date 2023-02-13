from odoo import models, fields

class User(models.Model):
    _name = "user"
    _description = "which store the differance type of users"

    name = fields.Char(required=True, string="Name")
    address = fields.Text(string="Address")
    phone_no = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")
    date_of_birth = fields.Date(string="Date of Birth")
    user_role = fields.Selection(
        string = "User Type",
        selection = [('customer','Customer'),('expert','Expert'),('employee','Employee')],
        help  = "Select which type of user"
        )
    
    # vendors vendor link
    vendor_id = fields.Many2one('product.vendor',string="Company Details")
    #doctor details
    experience = fields.Integer(required=True)
    clinic_address = fields.Text(string="Clinic address")
    clinic_phone_no = fields.Char(string="Clinic Phone No")
    clinic_mail = fields.Char(string="Clinic Email")




    

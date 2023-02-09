from odoo import models, fields

class User(models.Model):
    _name = "user"
    _description = "which store the differance type of users"

    name = fields.Char(required=True, string="Name")
    address = fields.Text(string="Address")
    phone_no = fields.Integer(string="Phone Number")
    email = fields.Char(string="Email")
    date_of_birth = fields.Date(string="Date of Birth")
    user_role = fields.Selection(
        string = "User Type",
        selection = [('customer','Customer'),('expert','Expert'),('employee','Employee')],
        help  = "Select which type of user"
        )
    
    vendors_id = fields.Integer(string="Company Details")

    experience = fields.Integer()
    clinic_address = fields.Text(string="Clinic address")
    clinic_phone_no = fields.Integer(string="Clinic Phone No")
    clinic_mail = fields.Char(string="Clinic Email")




    

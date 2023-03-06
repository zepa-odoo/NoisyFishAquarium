from odoo import models, fields

class ResUsers(models.Model):
    # _name = "aquarium.users"
    _description = "Type of user aquarium"
    _inherit = "res.users"
    _rec_name = "name"  

    user_role = fields.Selection(
        string = "User Type",
        selection = [('customer','Customer'),('expert','Expert'),('employee','Employee')],
        help  = "Select which type of user",
        
        )
    
    experience = fields.Integer(required=True)
    clinic_address = fields.Text(string="Clinic address")
    clinic_phone_no = fields.Char(string="Clinic Phone No")
    clinic_mail = fields.Char(string="Clinic Email")
    consultancy_fees = fields.Integer(string="Consultancy Fees")

    aquarium_vendor_id = fields.Many2one('aquarium.vendor', string="Company Name")

    
    

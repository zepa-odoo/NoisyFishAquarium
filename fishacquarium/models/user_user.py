from odoo import models, fields, api

class UserUser(models.Model):
    _name = "user.users"
    _description = "which store the differance type of users"

    name = fields.Char(required=True, string="Name")
    address = fields.Text(string="Address")
    phone_no = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")
    date_of_birth = fields.Date(string="Date of Birth")
    user_role = fields.Selection(
        string = "User Type",
        selection = [('customer','Customer'),('expert','Expert'),('employee','Employee')],
        help  = "Select which type of user",
        required=True
        )
    profile_img =  fields.Image(string="Profile Image", max_width=70, max_height=70)
    
    # vendors vendor link
    vendor_id = fields.Many2one('product.vendor',string="Company Details")
    vendor_address = fields.Text(string="Company Address", compute="_compute_vendor_address")
    vendor_email = fields.Char(string="Company Email Id", compute="_compute_vendor_email")
    vendor_phone_no = fields.Char(string="Company Contact Number",compute="_compute_vendor_phone_no")


    #doctor details
    experience = fields.Integer(required=True)
    clinic_address = fields.Text(string="Clinic address")
    clinic_phone_no = fields.Char(string="Clinic Phone No")
    clinic_mail = fields.Char(string="Clinic Email")

    #extra fields
    color = fields.Integer(string="Color", compute="_compute_color")


    @api.depends('vendor_id')
    def _compute_vendor_address(self):
        for record in self:
            record.vendor_address = record.vendor_id.company_address

    @api.depends('vendor_id')
    def _compute_vendor_email(self):
        for record in self:
            record.vendor_email = record.vendor_id.company_email

    @api.depends('vendor_id')
    def _compute_vendor_phone_no(self):
        for record in self:
            record.vendor_phone_no = record.vendor_id.phone_no

    @api.depends('user_role')
    def _compute_color(self):
        for record in self:
            if (record.user_role == 'customer'):
                record.color = 1
            elif(record.user_role == 'expert'):
                record.color = 2
            elif(record.user_role == 'employee'):
                record.color = 3

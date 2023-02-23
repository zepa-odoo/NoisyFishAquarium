from odoo import models, fields

class AquariumUser(models.Model):
    _name = "aquarium.user"
    _description = "Type of user aquarium"
    _rec_name = "partner_id"

    partner_id = fields.Many2one("res.partner")

    user_role = fields.Selection(
        string = "User Type",
        selection = [('customer','Customer'),('expert','Expert'),('employee','Employee')],
        help  = "Select which type of user",
        
        )
    

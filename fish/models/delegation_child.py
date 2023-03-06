from odoo import fields, models

class DelegationChild (models.Model):
    _name = "delegation.child"
    _description = "child"
    _inherit = 'delegation.parent'
    # _inherits = {'delegation.parent': 'delegation_parent_id'}

    delegation_parent_id = fields.Many2one('delegation.parent')
    
    color = fields.Integer()
    location = fields.Text()
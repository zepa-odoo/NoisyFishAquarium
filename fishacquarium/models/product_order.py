from odoo import fields,models,_
from datetime import datetime


# id_letter = 'A'
# id_no = '00001'

class ProductOrder(models.Model):
    _name = "product.order"
    _description = "order details"
    
    name = fields.Char(string='Order No', required=True, readonly=True, default=lambda self: _('New'), copy=False)
    user_id = fields.Many2one('user.users',string="Customer")
    product_ids = fields.Many2many('product.aquarium', string = "Products")
    state = fields.Selection(
        string = "Order Status",
        selection = [('preview','Preview'),('confirm','Confirm'),('address','Shipping Address'),('payment','Payment'),('ordered','Ordered'),('canceled','Canceled')] ,
        help = "Select the ordred stages"
    )
    totel_price = fields.Float(string = "Total")
    totel_quantity = fields.Integer(string = "Total Quantities")

    #for sequence
    def action_submit(self):
        self.ensure_one()
        if self.name == _('New'):
            self.name = self.env['ir.sequence'].next_by_code('product.order') or _('New')


    # ord() returns the corresponding ASCII value of character and after adding integer to it, 
    # chr() again converts it into character.
    # def _inverse_order_id(self):
    #     global id_letter
    #     global id_no
    #     for record in self:
    #         if(int(id_no)>9):
    #             id_letter = chr(ord(id_letter)+1)
    #             id_no = str(format(int('0')+1,'05d'))
    #         if(record.order_id == 'new'):
    #             record.order_id = id_letter + id_no
    #             id_no = str(format(int(id_no)+1,'05d'))
    #         print('.....................',record.order_id,'...............................')





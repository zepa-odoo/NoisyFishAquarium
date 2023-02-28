from odoo import fields,models

class ProductCategoryMedicine(models.Model):
    _name = "product.category.medicine"
    _description = "medicine category"

    name = fields.Char(required=True)
    # vendor_name = fields.Many2one('product.vendor',string="Vendor Name", required=True)
    product_description = fields.Text(string="Product Description")
    product_quantity = fields.Integer(string="Avaliable Product")
    product_price = fields.Float(string="Price")
    product_img = fields.Image(string="Product Image", max_width=70, max_height=70)
    product_color_id = fields.Many2one('product.color',string="Color")
    
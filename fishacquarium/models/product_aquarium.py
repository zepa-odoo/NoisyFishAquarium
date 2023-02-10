from odoo import fields,models

class ProductAquarium(models.Model):
    _name = "product.aquarium"
    _description = "Products for acquarium"

    vendor_name = fields.Many2one('product.vendor',string="Vendor Name")
    name = fields.Char(required = True, string="Product Title")
    product_description = fields.Text(string="Product Description")
    product_category = fields.Selection(
        string = "Product Category",
        selection = [('natural_product','Natural Product'),('artificial_product','Artificial Product')],
        help  = "Select which type of product",
        required=True
        )
    product_category_id = fields.Many2one('product.category.accessories',string="Artificial Product Category")
    product_price = fields.Float(string="Price")
    product_weight = fields.Float(string="Weight")
    product_height = fields.Float(string="height")
    product_length = fields.Float(string="Length")
    product_img = fields.Image(string="Product Image")
    product_color = fields.Many2many('product.color',string="Color")

    product_fish_category_id  = fields.Many2one('product.category.fish',string = "Fish Category")
    product_fish_food_id  = fields.Many2one('product.category.food',string = "Fish Food Category")
    product_fish_medicine_id  = fields.Many2one('product.category.medicine',string = "Fish Medicine Category")
    product_fish_water_id  = fields.Many2one('product.category.water',string = "Water Type")
    product_fish_lifespan  = fields.Integer(string = "Life Line")
    product_fish_size = fields.Integer(string = "Fish Size")
    
    



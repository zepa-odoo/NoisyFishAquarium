from odoo import fields,models

class ProductAquarium(models.Model):
    _name = "product.aquarium"
    _description = "Products for acquarium"

    
    name = fields.Char(required = True, string="Product Title")
    product_description = fields.Text(string="Product Description")
    product_category = fields.Selection(
        string = "Product Category",
        selection = [('natural_product','Natural Product'),('artificial_product','Artificial Product')],
        help  = "Select which type of product",
        required=True
        )
    vendor_name = fields.Many2one(
        'product.vendor',
        string="Vendor Name", 
        required=True,
        domain="['|',('product_production_type','=',product_category),('product_production_type','=','both')]"
        )
    product_quantity = fields.Integer(string="Avaliable Product")
    

    product_category_id = fields.Many2one('product.category.accessories',string="Artificial Product Category")
    product_price = fields.Float(string="Price")
    product_weight = fields.Float(string="Weight")
    product_height = fields.Float(string="height")
    product_length = fields.Float(string="Length")
    product_img = fields.Image(required=True, string="Product Image", max_width=70, max_height=70)
    product_color_ids = fields.Many2many('product.color',string="Color")

    product_fish_category_id  = fields.Many2one('product.category.fish',string = "Fish Category")
    product_fish_food_id  = fields.Many2one('product.category.food',string = "Fish Food Category")
    product_fish_medicine_ids  = fields.Many2many('product.category.medicine',string = "Fish Medicine Category")
    product_fish_water_ids  = fields.Many2many('product.category.water',string = "Water Type")
    product_fish_lifespan  = fields.Integer(string = "Life Line")
    product_fish_size = fields.Integer(string = "Fish Size")
    product_suitable_fish_ids = fields.Many2many('product.category.fish', string="Compatible Fishes")
    
    



from odoo import fields,models,api
from odoo.exceptions import ValidationError,UserError

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
    
    state = fields.Selection(
        string = "status",
        selection = [('new','New'),('farm','In Farm'),('warehouse','Ware House'),('available','Available'),('sold','Sold'),('live','Live'),('dead','Dead')],
        help  = "Select production stage",
        default="new"
        
        )
    
    aquairum_vendor_id = fields.Many2one(
        'aquarium.vendor',
        string="Vendor", 
        required=True,
        domain="['|',('product_production_type','=',product_category),('product_production_type','=','both')]"
        )
    product_quantity = fields.Integer(string="Avaliable Product")
    active = fields.Boolean("Active",default=True)
    
    product_category_id = fields.Many2one('product.category.accessories',string="Artificial Product Category")
    product_price = fields.Float(string="Price")
    product_weight = fields.Float(string="Weight")
    product_height = fields.Float(string="height")
    product_length = fields.Float(string="Length")
    product_img = fields.Image(required=True, string="Product Image", max_width=70, max_height=70)
    product_color_ids = fields.Many2many('product.color',string="Color")

    product_fish_category_id  = fields.Many2one('product.category.fish',string = "Fish Category")
    product_fish_food_id  = fields.Many2one('product.category.food',string = "Fish Food Category")
    product_fish_medicine_ids  = fields.One2many('product.category.medicine','product_aquarium_ids',string = "Fish Medicine Category")
    product_fish_water_ids  = fields.Many2many('product.category.water',string = "Water Type")
    product_fish_lifespan  = fields.Integer(string = "Life Line")
    product_fish_size = fields.Integer(string = "Fish Size")
    product_suitable_fish_ids = fields.Many2many("product.category.fish", string="Compatible Fishes", compute="_compute_product_suitable_fish_ids", readonly=False)

    _sql_constraints = [
        (
            'check_prices_possitive',
            'CHECK(product_price > 0.0)',
            "Product price are not be negative or zero(0) ."
        )
    ]

    @api.depends('product_fish_category_id')
    def _compute_product_suitable_fish_ids(self):
        for record in self:
            record.product_suitable_fish_ids = record.product_fish_category_id

    @api.constrains('product_quantity')
    def _check_selling_price(self):
        if (self.product_quantity<0):
            raise ValidationError('product quantity can not be negative ')
    
    def action_statusbar_new(self):
        for record in self:
            if (record.product_category == 'natural_product'):
                record.state = 'farm'
            elif (record.product_category == 'artificial_product'):
                record.state = 'warehouse'

    def action_statusbar_warehouse_available(self):
        for record in self:
            if(record.product_quantity <=0):
                raise UserError("Product Availaililly can not be Zero(0)")
            else:
                record.state = 'available'
    
    def action_statusbar_farm_live(self):
        for record in self:
            if(record.product_quantity <=0):
                raise UserError("Product Availaililly can not be Zero(0)")
            else:
                record.state = 'live'
            
    def action_statusbar_farm_dead(self):
        for record in self:
            record.state = 'dead'
            record.active= False
    
    def action_statusbar_warehouse_sold(self):
        for record in self:
            record.state = 'sold'
            record.active= False
        
            

    
    
    



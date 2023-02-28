from odoo import models, fields,api

class ProductCategory(models.Model):
    _name = 'product.category'
    _description = "All data of product categories"

    main_category = fields.Char(string = " Category ")
    sub_category = fields.Char(string = "Sub Category")
    

    _sql_constraints = [
        (
            'Check_combination_of_category_and_subCategory',
            'unique(main_category,sub_category)',
            'This category already available.'
        )
    ]

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "%s" % ( record.sub_category or '')))
        return result
    
   
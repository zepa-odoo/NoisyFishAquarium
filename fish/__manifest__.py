{
    'name' : "FishAcquarium",
    'version' : '1.0',
    'sequence' : 1,
    'application' : True,
    'depends' : [
        'base'
    ],
    'data' : [
        'security/ir.model.access.csv',
        
        'views/aquarium_user_view.xml',
        'views/product_aquarium_view.xml',
        'views/product_category_fish_view.xml',
        'views/product_category_food_view.xml',
        'views/product_category_medicine_view.xml',
        'views/product_category_water_view.xml',
        'views/product_category_accessories_view.xml',
        'views/product_color_view.xml',
        'views/aquarium_vendor_view.xml',
        'views/product_category.xml',
        'views/delegation_child_view.xml',
        'views/delegation_parent_view.xml',
        'views/aquarium_menu.xml'
        
    ]
    
}
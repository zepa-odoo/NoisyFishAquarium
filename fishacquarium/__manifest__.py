
{
    'name': "NoisyFishAquarium",
    'application': True,
    'sequance':-100,
    'version': '1.0',
    'depends': ['base'],
    'author': "ZEPA",
    'category': 'Category',
    'summary': """
      Self module Training
    """,
    'installable': True,
    'license': 'LGPL-3',

    'data':[
      'security/ir.model.access.csv',
      'data/ir_sequence_data.xml',
      'views/user_view.xml',
      'views/product_aquarium_view.xml',
      'views/product_category_fish_view.xml',
      'views/product_category_food_view.xml',
      'views/product_category_medicine_view.xml',
      'views/product_category_water_view.xml',
      'views/product_category_accessories_view.xml',
      'views/product_vendor_view.xml',
      'views/order_view.xml',
      'views/product_color_view.xml',

      'views/fishacquarium_menu.xml',
    ]   

}
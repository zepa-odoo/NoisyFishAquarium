
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
      'views/fishacquarium_menu.xml',
      'views/user_view.xml',
      'views/product_view.xml',
      'views/order_view.xml',

    ]   

}
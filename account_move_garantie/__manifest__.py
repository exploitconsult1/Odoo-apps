# -*- coding: utf-8 -*-
{
    'name': "account_move_garantie",

    'summary': """
        account_move_garantie""",

    'description': """
        Ajouter garantie au niveau de la facture
    """,
    'license' : 'LGPL-3',
    'author': "Exploit consult",
    'website': "http://exploit-consult.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Garanties',
    'version': '15.0.0.0.0.',
    'price' : '5.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode

    'images' : ['static/description/icon.png'],
}

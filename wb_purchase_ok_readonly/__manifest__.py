# -*- coding: utf-8 -*-

{
    'name': 'Purchase ok readonly',
    'version': '15.0.0.0',
    'author': 'Wonderbrands',
    'summary': 'Purchase ok readonly',
    'description': """""",
    'category': 'Base',
    'website': 'https://www.wonderbrands.com/',
    'license': 'AGPL-3',
    'depends': ['base', 'product','stock'],
    'data': [
        'data/ir_module_category_data.xml',
        'security/security.xml',
        'views/product_template.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

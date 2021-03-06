# -*- coding: utf-8 -*-
{
    'name': 'odoo_dev_traning',
    'version': '12.0.1.0',
    'summary': 'PS Cloud 培训',
    'author': "www.mypscloud.com",
    'website': 'https://www.mypscloud.com/',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/training_lesson_views.xml',
        'views/training_subject_views.xml',
        'views/training_views.xml',
    ],
    'demo': [
        'demo/pscloud_demo.xml',
    ],
    'qweb': [],
    'js': [],
    'css': [],
    'auto_install': False,
    'application': True
}
# -*- coding: utf-8 -*-
{
    'name': "Pharmacy Cost Profit Report",

    'summary': """
        
        """,

    'description': """
        
    """,

    'author': "Al Khidma Systems",
    'website': "http://www.alkhidmasystems.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','sale','pharmacy_management'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/report.xml',
        'views/sales_report.xml',
        'views/sales_report_wizard.xml',
    ],
}
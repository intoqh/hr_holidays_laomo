# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '休假模块继承',
    'version': '14.0',
    'summary': '休假模块继承，同一员工在俩个重叠的时间不能为请假',
    'author': "Laomo",
    'depends': ['hr_holidays'],
    'category': 'Hr',
    'sequence': 25,
    'data': [
        'views/hr_leave_allocation.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}

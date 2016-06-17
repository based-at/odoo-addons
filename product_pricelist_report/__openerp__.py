# -*- coding: utf-8 -*-
##############################################################################
#
#    Price List Report
#    Copyright (C) 2016 Vadim (<http://based.at>).
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2004-2016 Odoo S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Price list report',
    'version': '0.4',
    'depends': ['product'],
    'author': 'Vadim',
    'website': 'http://based.at',
    'category': 'Sales Management',
    'summary': 'Products list with prices',
    'description': """
Price list report
=================
Generates products list with prices. In a company with complicated product pricing (dealer price, retail price,
country-specific price, etc.) you may need to print/export a complete price list.

This module creates a model "product.pricelist.report" that inherits all columns from "product.product" module and ads
virtual columns per defined price list.

The report is available in "Sales -> Products -> Price Lists" menu. You can also export the prices if you have export enabled.

    """,
    "data": [
        'security/ir.model.access.csv',
        'security/report_security.xml',
        'views/pricelist_select.xml',
        'views/pricelist_report.xml',
        'views/templates.xml',
    ],
    'css': ['static/style.css'],
    'installable': True,
    'auto_install': False,
}

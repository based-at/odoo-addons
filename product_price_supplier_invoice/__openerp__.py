# -*- coding: utf-8 -*-
##############################################################################
#
#    Product price supplier invoice
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
    'name': 'Product Price from Invoice',
    'version': '0.1',
    'depends': ['product'],
    'author': 'Vadim',
    'website': 'http://based.at',
    'category': 'Sales Management',
    'description': """
Product price based on supplier invoice
=======================================
Add new price calculation based on latest validated supplier invoice price.

Your suppliers regularly change their prices? Simply set your formula to be based on 'Latest supplier invoice price'.
Book and validate a supplier invoice into the system and the base price is taken from this invoice.
If there is no supplier invoice containing the product you can set a price list to be used as default.

    """,
    "data": [
        'product_pricelist_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

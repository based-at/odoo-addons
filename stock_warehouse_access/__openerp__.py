# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Vadim (<http://based.at>).
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
    'name': 'Warehouse Access',
    'version': '0.1',
    'depends': ['stock_account'],
    'author': 'Vadim',
    'category': 'Warehouse Management',
    'summary': 'Limit user access to warehouses',
    'description': """
Warehouse Access
================
Restrict users access to warehouses.
    """,
    'website': 'http://based.at',
    "data": [
        'security/stock_access.xml',
        'stock_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

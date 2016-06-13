# -*- coding: utf-8 -*-
##############################################################################
#
#    Price List Access
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
    'name': 'Pricelist Access',
    'version': '0.1',
    'depends': ['sale'],
    'author': 'Vadim',
    'website': 'http://based.at',
    'category': 'Sales Management',
    'summary': 'Limit user access to price lists',
    'description': """
Pricelist Access
================
Restrict users access to particular price lists.

By default all Odoo users can access and select all available price lists.
In a company with complicated product pricing you may want to restrict user access to particular price lists.

To restrict user access, add the price lists to "Allowed Price Lists" field at the bottom of user edit form.
If the fields is empty, user can access all price lists.
    """,
    "data": [
        'security/pricelist_access.xml',
        'pricelist_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

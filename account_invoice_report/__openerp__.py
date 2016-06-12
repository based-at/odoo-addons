# -*- coding: utf-8 -*-
##############################################################################
#
#    Account Invoice Report
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
    'name': 'Account Invoice Report',
    'version': '0.1',
    'category': 'Accounting',
    'summary': 'Performance gain running "Invoices Analysis" report',
    'description': """
Account Invoice Report
======================
This module replaces standard account_invoice_report view with a snapshot (materialized view) to boost performance.
A cron job is scheduled to run every 30 minutes to refresh the snapshot.

Known issues:
    * Uninstall the module before attempting to update eInvoicing (account) module.
    """,
    'author': 'Vadim <vadim@based.at>',
    'website': 'http://based.at',
    'depends': ['account'],
    'data': ['account_invoice_report_view.xml'],
    'installable': True,
    'uninstall_hook': 'uninstall'
}

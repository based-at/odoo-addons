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

import sys
import psycopg2.extensions
from openerp.osv import fields, orm


class AccountInvoiceReport(orm.Model):
    _inherit = "account.invoice.report"

    def uninstall(self, cr, registry):
        cr.execute("DROP MATERIALIZED VIEW IF EXISTS %s" % (self._table,))
        super(AccountInvoiceReport, self).init(cr)

    def __init__(self, pool, cr):
        super(AccountInvoiceReport, self).__init__(pool, cr)
        setattr(sys.modules['openerp.addons.account_invoice_report'], 'uninstall', self.uninstall)

    def init(self, cr):
        try:
            cr.execute("DROP view IF EXISTS %s CASCADE" % (self._table,))
        except psycopg2.ProgrammingError:
            pass
        cr.commit()
        try:
            cr.execute("DROP MATERIALIZED VIEW IF EXISTS %s CASCADE" % (self._table,))
        except psycopg2.ProgrammingError:
            pass
        cr.commit()
        cr.execute("""CREATE MATERIALIZED VIEW %s as (
            WITH currency_rate (currency_id, rate, date_start, date_end) AS (
                SELECT r.currency_id, r.rate, r.name AS date_start,
                    (SELECT name FROM res_currency_rate r2
                     WHERE r2.name > r.name AND
                           r2.currency_id = r.currency_id
                     ORDER BY r2.name ASC
                     LIMIT 1) AS date_end
                FROM res_currency_rate r
            )
            %s
            FROM (
                %s %s %s
            ) AS sub
            JOIN currency_rate cr ON
                (cr.currency_id = sub.currency_id AND
                 cr.date_start <= COALESCE(sub.date, NOW()) AND
                 (cr.date_end IS NULL OR cr.date_end > COALESCE(sub.date, NOW())))
        )""" % (
                    self._table,
                    self._select(), self._sub_select(), self._from(), self._group_by()))

    def refresh(self, cr, uid, ids=None, context=None):
        cr.execute("REFRESH MATERIALIZED VIEW %s" % (self._table,))

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

from openerp import models, fields
from openerp.tools.safe_eval import safe_eval


class ProductPricelistSelect(models.TransientModel):
    _name = 'product.pricelist.select'
    _description = 'Price List Selection'

    pricelist_ids = fields.Many2many('product.pricelist', 'product_pricelist_select_rel', 'rep_id', 'pl_id',
                                     string='Price lists', required=True)

    def view_report(self, cr, uid, ids, context=None):
        for report in self.browse(cr, uid, ids, context=context):
            view, res_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'product_pricelist_report',
                                                                               'action_product_pricelist_report')
            result = self.pool.get(view).read(cr, uid, [res_id], context=context)[0]
            ctx = safe_eval(result.get('context', '{}'))
            ctx.update({'pricelist_ids': [pl.id for pl in report.pricelist_ids]})
            result.update({'context': ctx})
            return result

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

from lxml import etree
from openerp import tools
import openerp.addons.decimal_precision as dp
from openerp import models, fields, exceptions, api


class ProductPricelistReport(models.Model):
    _name = 'product.pricelist.report'
    _description = 'Price List Report'
    _inherits = {'product.product': 'product_id'}
    _auto = False

    product_id = fields.Many2one('product.product', required=True, readonly=True)

    @api.multi
    def _price_get(self, pl_id=1):
        for product in self:
            price = 0.0
            try:
                price = self.env['product.pricelist'].browse(pl_id).price_get(product.id, 1)[pl_id]
            except exceptions.AccessError:
                pass
            finally:
                setattr(product, '$pl_' + str(pl_id), price)

    @classmethod
    def price_get(cls, pl_id):
        return lambda *args: cls._price_get(*args, pl_id=pl_id)

    @classmethod
    def _build_model(cls, pool, cr):
        cr.execute("SELECT p.id, p.name||' ('|| c.name ||')' "
                   " FROM product_pricelist p JOIN res_currency c ON c.id=p.currency_id")
        # Bind price list entries
        for pl, name in cr.fetchall():
            setattr(cls, '$pl_' + str(pl), fields.Float(string=name, digits=dp.get_precision('Product Price'),
                                                        compute=cls.price_get(pl)))
        return super(ProductPricelistReport, cls)._build_model(pool, cr)

    def fields_get(self, cr, uid, allfields=None, context=None, write_access=True):
        """ Restrict access
        """
        res = super(ProductPricelistReport, self).fields_get(cr, uid, allfields=allfields, context=context, write_access=write_access)
        pl_obj = self.pool.get('product.pricelist')
        pl_ids = pl_obj.search(cr, uid, [], context=context)
        for field in res.copy():
            if field.startswith('$pl_') and int(field.split('_')[1]) not in pl_ids:
                res.pop(field, None)
        return res

    def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=None, toolbar=False, submenu=False):
        context = context or {}
        res = super(ProductPricelistReport, self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type,
                                                                  context=context, toolbar=toolbar, submenu=submenu)
        if view_type == 'tree':
            doc = etree.XML(res['arch'])
            for pl in self.pool.get('product.pricelist').browse(cr, uid, context.get('pricelist_ids', []), context=context):
                res['fields'].update({
                    '$pl_' + str(pl.id): {
                        'string': pl.name + ' (' + pl.currency_id.name + ')',
                        'type': 'float', 'readonly': True, 'store': False, 'states': {}, 'views': {}
                    }
                })
                for tree in doc.xpath("//tree"):
                    field = etree.SubElement(tree, 'field')
                    field.set('name', '$pl_' + str(pl.id))
                    field.set('modifiers', '{"readonly": true}')
            res['arch'] = etree.tostring(doc)
        return res

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'product_pricelist_report')
        cr.execute("CREATE VIEW product_pricelist_report AS"
                   " SELECT id, id AS product_id FROM product_product")

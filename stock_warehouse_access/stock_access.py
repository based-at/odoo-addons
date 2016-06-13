# -*- coding: utf-8 -*-
##############################################################################
#
#    Limit User Access per Warehouse
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

from openerp import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.one
    def _get_location_ids(self):
        """ Get the list of locations that either not attached to a warehouse (virtual location, asset Location)
                OR user has access to the warehouse this location belongs to
        """
        locations = self.env['stock.location'].search([])
        if self.warehouse_ids:
            # Allow locations that are not attached to a warehouse
            w_ids = [False] + [w.id for w in self.warehouse_ids]
            locations = locations.filtered(lambda r: locations.get_warehouse(r) in w_ids)
        self.location_ids = locations

    warehouse_ids = fields.Many2many('stock.warehouse', string='Allowed Warehouses',
                                     help='List of allowed warehouses. If empty, the user can access all warehouses.')
    location_ids = fields.One2many('stock.location', string='Allowed Locations', compute='_get_location_ids')


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    @api.one
    def _get_user_ids(self):
        """ Get the list of "Warehouse / Users" who can access this warehouse
        """
        user_ids = [user.id for user in self.env['ir.model.data'].xmlid_to_object('stock.group_stock_user').users
                    if not user.warehouse_ids or self in user.warehouse_ids]
        self.user_ids = user_ids

    user_ids = fields.One2many('res.users', string='Authorized Users', compute='_get_user_ids',
                               help='List of users authorized to access the warehouse.')

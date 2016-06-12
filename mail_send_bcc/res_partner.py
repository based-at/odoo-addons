# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class ResPartner(osv.Model):
    """ Add preference field """
    _inherit = 'res.partner'

    _columns = {
        'notification_receive_copy':
            fields.boolean('Bcc Sent Messages',
                           help="If this option is checked you will receive a blind carbon copy of sent messages to your email address")
    }

    _defaults = {
        'notification_receive_copy': False,
    }

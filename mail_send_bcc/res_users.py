# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class ResUsers(osv.Model):
    """ Override __init__ to allow notification_receive_copy modification """
    _inherit = 'res.users'

    def __init__(self, pool, cr):
        """ Override of __init__ to add access rights on notification_receive_copy field
            Shamelessly ripped off mail/res_user.py:__init__
        """
        result = super(ResUsers, self).__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        self.SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        self.SELF_WRITEABLE_FIELDS.append('notification_receive_copy')
        # duplicate list to avoid modifying the original reference
        self.SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        self.SELF_READABLE_FIELDS.append('notification_receive_copy')
        return result

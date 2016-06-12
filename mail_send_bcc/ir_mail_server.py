# -*- coding: utf-8 -*-

from openerp.osv import osv
from email.utils import COMMASPACE
from openerp.addons.base.ir.ir_mail_server import encode_rfc2822_address_header, extract_rfc2822_addresses


class IrMailServer(osv.Model):
    _inherit = "ir.mail_server"

    def send_email(self, cr, uid, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False,
                   context=None):
        """ Send blind carbon copy to message originator
                apparently uid is SUPERUSER_ID, real uid comes in context
        """
        real_uid = (context or {}).get('uid')
        user = self.pool.get('res.users').browse(cr, uid, real_uid, context=context)
        if real_uid and user.partner_id.notification_receive_copy:
            bcc_list = extract_rfc2822_addresses(message['Bcc'])
            bcc = user.email or '%s@%s' % (user.alias_name, user.alias_domain) if user.alias_domain else None
            if bcc:
                message['Bcc'] = encode_rfc2822_address_header(COMMASPACE.join(bcc_list + [bcc]))
        return super(IrMailServer, self).send_email(cr, uid, message, mail_server_id, smtp_server, smtp_port,
                                                    smtp_user, smtp_password, smtp_encryption, smtp_debug, context)

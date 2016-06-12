# -*- coding: utf-8 -*-

{
    'name': 'Send Bcc',
    'version': '0.2',
    'category': 'Social Network',
    'summary': 'Send Bcc to message originator',
    'description': """
Send BCC to message originator
==============================
Override default behaviour when sending email: send a blind carbon copy to the message originator.
    """,
    'author': 'Vadim <vadim@based.at>',
    'website': 'http://based.at',
    'depends': ['mail'],
    'data': ['res_users_view.xml'],
    'installable': True,
}

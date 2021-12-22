# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-
from odoo import models, fields

class User(models.Model):
    _inherit= 'res.user'
    birthDate=fields.Date()
    status= fields.Selection(PRIVILEGE_SELECTION)
    PRIVILEGE_SELECTION = [
        ('0', 'USER'),
        ('1', 'ADMIN'),
        ('2', 'STUDENT'),
        ('3', 'TEACHER'),
    ]



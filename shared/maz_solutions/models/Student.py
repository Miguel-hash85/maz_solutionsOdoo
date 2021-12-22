# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  Student(models.Model):
   
    _name= 'maz_solutions.Student'
    _inherit= 'maz_solutions.user'
    year=fields.Date()
    sessions=fields.One2Many('maz_solutions.sessions','examSession',string="Sessions")
    course=fields.Many2One('maz_solutions.Course',string="Course")



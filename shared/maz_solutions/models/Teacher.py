# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class Teacher (models.Model):
    
    _inherit='res.users'
    
    _name='maz_solutions.teacher'
    
    salary=fields.Float()
    
    teacher_courses=fields.One2many('maz_solutions.teacher_course','teacher',string="Teacher Course")

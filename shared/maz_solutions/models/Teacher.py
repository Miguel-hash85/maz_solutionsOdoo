# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class Teacher (models.Model):
    
    _inherit='res.user'
    
    _name='maz_solutions.Teacher'
    
    salary=fields.Float()
    
    teacherCourses=fields.One2Many('maz_solutions.TeacherCourse','Teacher',string="Teacher Course")

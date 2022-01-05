# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  TeacherCourse(models.Model):
    _name='maz_solutions.teacher_course'
     
    name=fields.Char()
    
    dateStart=fields.Date()
    
    dateEnd=fields.Date()
    
    teacher=fields.Many2one('maz_solutions.teacher',string="Teacher")
    
    teacher_course_subject=fields.One2many('maz_solutions.teacher_course_subject','teacher_course',string="Teacher Course Subject")
   

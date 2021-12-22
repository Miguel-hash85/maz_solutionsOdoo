# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  TeacherCourseSubject(models.Model):
    
    _name='maz_solutions.TeacherCourseSubject'

    totalHours=fields.Float()
    
   # subject=fields.Many2One('maz_solutions.Subject',string="Subject")
    
   # teacherCourse=fields.Many2One('maz_solutions.TeacherCourse',string="TeacherCourse")
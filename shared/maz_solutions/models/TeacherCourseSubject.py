# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  TeacherCourseSubject(models.Model):
    
    _name='maz_solutions.teacher_course_subject'

    totalHours=fields.Float()
    
    subject=fields.Many2one('maz_solutions.subject',string="Subject")
    
    teacher_course=fields.Many2one('maz_solutions.teacher_course',string="Teacher Course")
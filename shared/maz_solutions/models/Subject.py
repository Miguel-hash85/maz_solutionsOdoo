# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  Subject(models.Model):
   
    _name='maz_solutions.subject'
     
    name=fields.Char()
    
    password=fields.Char()
    
    teacher_course_subjects=fields.One2many('maz_solutions.teacher_course_subject','subject',string="Teacher Course Subjects")
    
    exams=fields.One2many('maz_solutions.exam','subject',string="Exams")
    
    course_subjects=fields.One2many('maz_solutions.course_subject','subject',string="Course Subjects")
    
    
    
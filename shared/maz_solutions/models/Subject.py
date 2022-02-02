# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields,api,exceptions

class  Subject(models.Model):
   
    _name='maz_solutions.subject'
     
    name=fields.Char()
    
    total_hours=fields.Float()
    
    teacher_course_subjects=fields.One2many('maz_solutions.teacher_course_subject','subject',string="Teacher Course Subjects")
    
    exams=fields.One2many('maz_solutions.exam','subject',string="Exams")
    
    course_subjects=fields.One2many('maz_solutions.course_subject','subject',string="Course Subjects")
    
    @api.constrains('total_hours')
    def _check_date_values(self):
        for record in self:
            if record.total_hours < 0:
                raise exceptions.ValidationError("The value of total hours must be positive")
             
    @api.constrains('name')
    def _check_name_is_not_empty(self):
        for record in self:
            if (not (record.name and record.name.strip())):
                 raise exceptions.ValidationError("The name has to have a value")       
    
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields,api,exceptions

class  TeacherCourse(models.Model):
    _name='maz_solutions.teacher_course'
     
    name=fields.Char()
    
    date_Start=fields.Date()
    
    date_End=fields.Date()
    
    teacher=fields.Many2one('maz_solutions.teacher',string="Teacher")
    
    teacher_course_subject=fields.One2many('maz_solutions.teacher_course_subject','teacher_course',string="Teacher Course Subject")
   
    @api.constrains('date_Start','date_End')
    def _check_date_values(self):
        for record in self:
            if record.date_Start > record.date_End:
               raise exceptions.ValidationError("The date end has to be at least, a day after date_start")
    @api.constrains('name')
    def _check_name_is_not_empty(self):
        for record in self:
            if (not (record.name and record.name.strip())):
                raise exceptions.ValidationError("The name has to have a value")         
    @api.onchange('name')
    def _validation_name_length(self):
        if len(str(self.name)) > 50:
            return {
                'warning': {
                    'title': "Maximun limit arrive",
                    'message': "You have reached the maximum character limit",
                },
            }
    @api.onchange('date_Start','date_End')
    def _validation_dates(self):
        if self.date_Start == self.date_End:
            return {
                'warning': {
                    'title': "Dates Validation",
                    'message': "The date start must be before the date end",
                },
            }        
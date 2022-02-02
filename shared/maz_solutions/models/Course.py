# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields,api

class  Course(models.Model):
   
    _name='maz_solutions.course'
    name=fields.Char()   
    dateStart=fields.Date()
    dateEnd=fields.Date()
    course_subject=fields.One2many('maz_solutions.course_subject','course',string="Course Subject")
    students=fields.One2many('maz_solutions.student','course',string="Student")
    

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

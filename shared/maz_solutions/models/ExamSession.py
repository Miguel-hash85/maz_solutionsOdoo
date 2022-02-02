# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api
from odoo.exceptions import  ValidationError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime

class ExamSession (models.Model):
    
    _name='maz_solutions.exam_session'
    
    dateTimeStart=fields.Datetime()
    
    dateTimeEnd=fields.Datetime()
    
    student=fields.Many2one('maz_solutions.student', string="Student")
    
    exam=fields.Many2one('maz_solutions.exam', string="Exam")
    
    mark=fields.Integer()

    @api.constrains('dateTimeEnd','dateTimeStart')
    def _check_dates(self):
        for record in self:
            if record.dateTimeStart > record.dateTimeEnd:
                raise ValidationError("Sorry, End date must be greater that Start date")
            
    @api.constrains('mark')
    def _check_mark(self):
        for record in self:
            if record.mark > 10:
                raise ValidationError("Sorry, mark should not be greater than 10")
            if record.mark < 0:
                raise ValidationError("Sorry, mark should not be lower than 0")
    
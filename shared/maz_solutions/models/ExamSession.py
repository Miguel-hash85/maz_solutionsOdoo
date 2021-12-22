# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class ExamSession (models.Model):
    
    _name='maz_solutions.ExamSession'
    
    dateTimeStart=fields.Datetime()
    
    dateTimeEnd=fields.Datetime()
    
#    student=fields.Many2one('maz_solutions.Student', string="Student")
    
#    exam=fields.Many2One('maz_solutions.Exam', string="Exam")
    
    mark=fields.Integer()

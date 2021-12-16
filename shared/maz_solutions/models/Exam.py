# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class Exam (models.Model):
    
    _name='maz_solutions.Exam'
    
    statment=fields.Text()
    
    subject=fields.Many2One('maz_solutions.Subject', string="Subject")
    
    examSessions=fields.One2Many('maz_solutions.ExamSession','Exam', string="ExamSessions")

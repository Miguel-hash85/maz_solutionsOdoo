# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class Exam (models.Model):
    
    _name='maz_solutions.exam'
    
    statement=fields.Text()
    
    subject=fields.Many2one('maz_solutions.subject', string="Subject")
  
    exam_sessions=fields.One2many('maz_solutions.exam_session','exam', string="ExamSessions")

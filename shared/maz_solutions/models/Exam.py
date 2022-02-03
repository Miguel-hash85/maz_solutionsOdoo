# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields,api

class Exam (models.Model):
    
    _name='maz_solutions.exam'
    
    statement=fields.Text()
    
    subject=fields.Many2one('maz_solutions.subject', string="Subject")
  
    exam_sessions=fields.One2many('maz_solutions.exam_session','exam', string="ExamSessions")
    
    @api.constrains('statement')
    def _statement_is_not_empty(self):
        for record in self:
            if (not (record.statement and record.statement.strip())):
                raise exceptions.ValidationError("The statement has to have a value")
            
    @api.onchange('statement')
    def _statement_maximun_character_arrived(self):
        if len(str(self.statement)) > 50:
            return {
                'warning': {
                    'title': "Invalid statement",
                    'message': "Maximun character limit arrived!",
                },
            }
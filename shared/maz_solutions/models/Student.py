# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  Student(models.Model):
   
    _name= 'maz_solutions.student'
    _inherit='res.users'
    year=fields.Date()
    sessions=fields.One2many('maz_solutions.exam_session','student',string="Exam Sessions")
    course=fields.Many2one('maz_solutions.course',string="Course")
    
    @api.constrains('year')
    def _check_something(self):
        for record in self:
            if record.year > date.today():
                raise ValidationError("Incorrect year")



# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions

class Teacher (models.Model):
    
    _inherit = 'res.users'
    
    _name = 'maz_solutions.teacher'
    
    salary = fields.Float()
    
    teacher_courses = fields.One2many('maz_solutions.teacher_course', 'teacher', string="Teacher Course")
    
    @api.constrains('salary')
    def _check_salary_value(self):
        for record in self:
            if record.salary <= 0:
                raise exceptions.ValidationError("The salary must be positive")
    @api.onchange('salary')
    def _validation_salary_length(self):
        if not len(str(self.salary)) > 5:
            return {
                'warning': {
                    'title': "Invalid salary",
                    'message': "The minimum salary is 100",
                },
            }
    @api.onchange('name')
    def _validation_name_length(self):
        if(len(str(self.name))) > 50:
            return {
                'warning': {
                    'title': "Maximun limit arrive",
                    'message': "You have reached the maximum character limit",
                },
            }        
    
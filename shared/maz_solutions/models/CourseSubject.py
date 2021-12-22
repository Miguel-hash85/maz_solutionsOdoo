# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class CourseSubject (models.Model):

    _name='maz_solutions.CourseSubject'
    
    course=fields.Many2One('maz_solutions.Course',string="Course")
    
    subject=fields.Many2One('maz_solutions.Subject',string="Subject")
    
    
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class CourseSubject (models.Model):

    _name='maz_solutions.course_subject'
    
    course=fields.Many2one('maz_solutions.course',string="Course")
    
    subject=fields.Many2one('maz_solutions.subject',string="Subject")
    
    
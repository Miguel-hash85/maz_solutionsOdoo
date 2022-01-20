# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  Course(models.Model):
   
    _name='maz_solutions.course'
    name=fields.Char()   
    dateStart=fields.Date()
    dateEnd=fields.Date()
    course_subject=fields.One2many('maz_solutions.course_subject','course',string="Course Subject")
    students=fields.One2many('maz_solutions.student','course',string="Student")
    



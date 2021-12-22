# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  Course(models.Model):
   
    _name='maz_solutions.Course'
    name=fields.Char   
    dateStart=fields.Date()
    dateEnd=fields.Date()
#    courseSubjects=fields.One2Many('maz_solutions.CourseSubject','subject',string="CourseSubjects")
#    students=fields.One2Many('maz_solutions.Student','Student',string="Students")
    



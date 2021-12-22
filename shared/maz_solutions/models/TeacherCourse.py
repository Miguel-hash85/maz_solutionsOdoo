# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class  TeacherCourse(models.Model):
    _name='maz_solutions.TeacherCourse'
     
    name=fields.Char()
    
    dateStart=fields.Date()
    
    dateEnd=fields.Date()
    
  #  teacher=fields.Many2One('maz_solutions.Teacher',string="Teacher")
    
  #  subjects=fields.One2Many('maz_solutions.Subject',teacherCourse,string="Subjects")
    
    
   

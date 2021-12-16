# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class  Student(models.Model):
   
    _name= 'Res.Student'
    _inherit= 'Res.User'
    year=fields.Date()
    sessions=fields.One2Many('maz_solutions.sessions','examSession',string="Sessions")
    Course=fields.Many2One('maz_solutions.Course',string="Course")



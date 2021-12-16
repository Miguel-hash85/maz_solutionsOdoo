# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class  Course(models.Model):
   
    _name='maz_solutions.Course'
    name=fields.Char   
    dateStart=fields.Date()
    dateEnd=fields.Date()
    CourseSubjects=fields.One2Many('maz_solutions.CourseSubject','Subject',string="CourseSubjects")
    Students=fields.One2Many('maz_solutions.CourseSubject','Student',string="Students")
    



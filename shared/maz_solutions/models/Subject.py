# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class  Subject(models.Model):
   
    _name='maz_solutions.Subject'
     
    name=fields.Char()
    
    password=fields.Char()
    
    teacherCourseSubjects=fields.One2Many('maz_solutions.TeacherCourseSubject','Subject',string="TeacherCourseSubjects")
    
    exams=fields.One2Many('maz_solutions.Exam','Exam',string="Exams")
    
    courseSubjects=fields.One2Many('maz_solutions.CourseSubject','CourseSubject',string="CourseSubjects")
    
    
    
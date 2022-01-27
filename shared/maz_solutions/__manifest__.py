# -*- coding: utf-8 -*-
{
    'name': "Maz Solutions",

    'summary': """
        Module to manage the academic issues.
        """,

    'description': """
        To manage the academic issues, we are focused on diferent entities:
            -User: Generic user of our application.
            -Teacher: The ones who teaches subjects, create exams and exam sessions.
            -Student: They can take part in exam, and diferent courses.
            -TeacherCourse: Formed by teachers, subjects and different dates of ending and start.
            -Course: Formed by students, subjects and different dates of ending and start.
            -Subjects: Where we can store different teachers, courses and exams.
            -Exam: It can have different exam sessions and a subject.
            -ExamSession: Formed by a student, an exam and different dates of ending and start.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/maz_solutions_view.xml',
        'views/templates.xml',
        'views/admin_student_view.xml',
        'views/admin_course_view.xml',
        'views/subject_view.xml',
        'views/admin_teacher_view.xml',
        'views/teacher_course_view.xml',
        'report/teacher_admin_course_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
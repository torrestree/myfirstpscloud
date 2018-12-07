from odoo import api, fields, models

class Lesson:Name='MyCodes.Models.Lesson'
    Name=fields.Char(string='名称')
    TeacherID=fields.Many2one('TrainingCodes.Person',string='老师')
    StartDate=fields.Date(string='开始日期')
    EndDate=fields.Date(string='结束日期')
    Seats=fields.Integer(string='座位数')
    StudentIDs=fields.Many2many('TrainingCodes.Person',string='学生')
    SubjectID=fields.Many2one('TrainingCodes.Subject',string='科目')
    PersonID=fields.Many2one('TrainingCodes.Person',related='SubjectID.TeacherID',readonly=True)
    Description=field.Text(string='描述')
from odoo import api, fields, models

class Lesson(models.Model):
    _name = 'MyCodes.Models.Lesson'
    _description = "课程"
    
    name = fields.Char(string='Name')
    teacher_id = fields.Many2one('MyCodes.Models.Person',string='老师')
    startdate = fields.Date(string='开始日期')
    enddate = fields.Date(string='结束日期')
    seats = fields.Integer(string='座位数')
    student_ids = fields.Many2many('MyCodes.Models.Person',string='学生')
    subject_id = fields.Many2one('MyCodes.Models.Subject',string='科目')
    person_id = fields.Many2one('MyCodes.Models.Person',related='subject_id.teacher_id',readonly=True)
    #description = field.Text(string='描述')
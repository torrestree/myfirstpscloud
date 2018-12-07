from odoo import api, fields, models

class Subject(models.Model):Name='MyCodes.Models.Lesson'
    Name=fields.Char(string='名称')
    TeacherID=fields.Many2one('TrainingCodes.Person',string='负责人')
    LessonIDs=fields.One2many('TrainingCodes.Lesson',string='课程')
    Description=fields.Text(string='描述')
    State = fields.Selection([('draft', '草稿'),('confirm', '确认')], string='状态', readonly=True, copy=False, index=True, default='draft')
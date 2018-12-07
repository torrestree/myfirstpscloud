from odoo import api, fields, models

class Subject(models.Model):
    _name = 'MyCodes.Models.Lesson'
    _description = "科目"
    
    name = fields.Char(string='Name')
    teacher_id = fields.Many2one('MyCodes.Models.Person',string='负责人')
    lesson_ids = fields.One2many('MyCodes.Models.Lesson',string='课程')
    description = fields.Text(string='描述')
    state = fields.Selection([('draft', '草稿'),('confirm', '确认')], string='状态', readonly=True, copy=False, index=True, default='draft')